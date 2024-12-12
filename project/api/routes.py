"""
API routes for the voice assistant
"""
import shutil
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional
from fastapi import APIRouter
from api.endpoints import process_command

from services.voice_recognition import transcribe_audio


app = FastAPI()
app = APIRouter()

app.include_router(process_command.router, prefix="/process-command", tags=["commands"])

class CommandRequest(BaseModel):
    audio_file: str
    user_id: Optional[int]

@app.post("/process-command")
async def process_command(command_request: CommandRequest):
    # Process voice command logic here
    import shutil
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Optional

# Assuming the existence of the `voice_recognition.py` service
from services.voice_recognition import transcribe_audio

app = FastAPI()

class CommandRequest(BaseModel):
    audio_file: str
    user_id: Optional[int]

@app.post("/process-command")
async def process_command(command_request: CommandRequest):
    # Process voice command logic here
    # For demonstration purposes, let's assume the `audio_file` contains the transcribed text
    transcribed_text = command_request.audio_file

    # You can now use the `transcribed_text` for further processing or analysis
    # For example, you can use natural language processing (NLP) techniques to understand the user's command
    # ...

    return {"transcribed_text": transcribed_text}
    pass

@app.post("/upload-audio")
async def upload_audio(file: UploadFile = File(...)):
    # Handle audio file upload
    # Save the uploaded file to a temporary location
    temp_file_path = f"temp_uploads/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Process the uploaded audio file
    # You can use the `temp_file_path` to perform further operations on the audio file
    # For example, you can use the `voice_recognition.py` service to transcribe the audio file
    transcribed_text = await transcribe_audio(temp_file_path)

    # Return the transcribed text as a response
    return {"transcribed_text": transcribed_text}
    pass