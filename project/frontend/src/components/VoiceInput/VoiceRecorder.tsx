import React, { useCallback } from 'react';
import { Button, CircularProgress, Alert } from '@mui/material';
import MicIcon from '@mui/icons-material/Mic';
import StopIcon from '@mui/icons-material/Stop';
import { styled } from '@mui/system';
import { useAudioRecorder } from '../../hooks/useAudioRecorder';
import { processVoiceCommand } from '../../utils/api';

const RecordButton = styled(Button)(({ theme }) => ({
  borderRadius: '50%',
  width: '64px',
  height: '64px',
  minWidth: 'unset',
  '&.recording': {
    backgroundColor: theme.palette.error.main,
    '&:hover': {
      backgroundColor: theme.palette.error.dark,
    },
  },
}));

interface VoiceRecorderProps {
  onRecordingComplete: (blob: Blob) => void;
}

const VoiceRecorder: React.FC<VoiceRecorderProps> = ({ onRecordingComplete }) => {
  const { 
    isRecording, 
    error, 
    startRecording, 
    stopRecording 
  } = useAudioRecorder();

  const handleToggleRecording = useCallback(async () => {
    if (isRecording) {
      const audioBlob = await stopRecording();
      if (audioBlob) {
        onRecordingComplete(audioBlob);
      }
    } else {
      await startRecording();
    }
  }, [isRecording, startRecording, stopRecording, onRecordingComplete]);

  if (error) {
    return (
      <Alert severity="error" className="mb-4">
        {error}
      </Alert>
    );
  }

  return (
    <div className="flex flex-col items-center gap-4">
      <RecordButton
        variant="contained"
        className={isRecording ? 'recording' : ''}
        onClick={handleToggleRecording}
        disabled={!!error}
      >
        {isRecording ? <StopIcon /> : <MicIcon />}
      </RecordButton>
      <span className="text-sm text-gray-600">
        {isRecording ? 'Recording...' : 'Click to start recording'}
      </span>
    </div>
  );
};