import { Command } from '../types/command';

const API_BASE_URL = '/api';

interface ApiResponse<T> {
  data?: T;
  error?: string;
}

export const processVoiceCommand = async (
  audioBlob: Blob
): Promise<ApiResponse<Command>> => {
  try {
    const formData = new FormData();
    formData.append('audio', audioBlob);

    const response = await fetch(`${API_BASE_URL}/process-command`, {
      method: 'POST',
      body: formData,
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    });

    if (!response.ok) {
      throw new Error('Failed to process command');
    }

    const data = await response.json();
    return { data };
  } catch (error) {
    return { 
      error: error instanceof Error ? error.message : 'An error occurred' 
    };
  }
};