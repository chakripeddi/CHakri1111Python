export const createAudioStream = async (): Promise<MediaStream> => {
  try {
    return await navigator.mediaDevices.getUserMedia({ 
      audio: true,
      video: false
    });
  } catch (error) {
    throw new Error('Failed to access microphone');
  }
};

export const stopAudioStream = (stream: MediaStream): void => {
  stream.getTracks().forEach(track => track.stop());
};