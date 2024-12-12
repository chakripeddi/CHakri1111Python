# services/voice_recognition.py

import whisper
from typing import Optional


class VoiceRecognitionService:
    def recognize_command(self, processed_command):
        # Implement voice recognition logic here
        # Convert the processed command into a standard format
        # Return the recognized command
        recognized_command = "Recognized command: " + processed_command
        return recognized_command

class VoiceRecognizer:
    def __init__(self, model_name: str = "base"):
        self.model = whisper.load_model(model_name)
    
    async def transcribe_audio(self, audio_file: str) -> Optional[str]:
        try:
            result = await self.model.transcribe(audio_file)
            return result["text"]
        except Exception as e:
            print(f"Error transcribing audio: {e}")
            return None