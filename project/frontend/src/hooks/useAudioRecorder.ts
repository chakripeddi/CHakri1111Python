import { useState, useCallback } from 'react';
import { createAudioStream, stopAudioStream } from '../utils/audioUtils';

interface AudioRecorderState {
  isRecording: boolean;
  error: string | null;
}

export const useAudioRecorder = () => {
  const [state, setState] = useState<AudioRecorderState>({
    isRecording: false,
    error: null
  });
  const [mediaRecorder, setMediaRecorder] = useState<MediaRecorder | null>(null);
  const [audioChunks, setAudioChunks] = useState<Blob[]>([]);

  const startRecording = useCallback(async () => {
    try {
      const stream = await createAudioStream();
      const recorder = new MediaRecorder(stream);
      
      recorder.ondataavailable = (event) => {
        if (event.data.size > 0) {
          setAudioChunks(chunks => [...chunks, event.data]);
        }
      };

      recorder.start();
      setMediaRecorder(recorder);
      setState({ isRecording: true, error: null });
    } catch (error) {
      setState({ 
        isRecording: false, 
        error: error instanceof Error ? error.message : 'Recording failed' 
      });
    }
  }, []);

  const stopRecording = useCallback(async (): Promise<Blob | null> => {
    if (!mediaRecorder) return null;

    return new Promise((resolve) => {
      mediaRecorder.onstop = () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/webm' });
        setAudioChunks([]);
        resolve(audioBlob);
      };

      mediaRecorder.stop();
      if (mediaRecorder.stream) {
        stopAudioStream(mediaRecorder.stream);
      }
      setState({ isRecording: false, error: null });
    });
  }, [mediaRecorder, audioChunks]);

  return {
    isRecording: state.isRecording,
    error: state.error,
    startRecording,
    stopRecording
  };
};