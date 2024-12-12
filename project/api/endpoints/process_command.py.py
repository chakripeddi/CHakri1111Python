from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.nlp import NLPService
from services.voice_recognition import VoiceRecognitionService
from services.web_automation import WebAutomationService
from services.user_preferences import UserPreferencesService



class CommandInput(BaseModel):
    voice_command: str

class CommandOutput(BaseModel):
    success: bool
    message: str
    result: str


router = APIRouter()

@router.post("/", response_model=CommandOutput)
async def process_voice_command(command_input: CommandInput):
    voice_command = command_input.voice_command

    # Perform natural language processing
    nlp_service = NLPService()
    processed_command = nlp_service.process_command(voice_command)

    # Perform voice recognition
    voice_recognition_service = VoiceRecognitionService()
    recognized_command = voice_recognition_service.recognize_command(processed_command)

    # Perform web automation
    web_automation_service = WebAutomationService()
    automation_result = web_automation_service.perform_action(recognized_command)

    # Manage user preferences
    user_preferences_service = UserPreferencesService()
    preferences = user_preferences_service.get_preferences()
    adjusted_result = user_preferences_service.apply_preferences(automation_result, preferences)

    return CommandOutput(success=True, message="Command processed successfully", result=adjusted_result)