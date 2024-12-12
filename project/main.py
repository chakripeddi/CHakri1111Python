"""
Main application entry point
"""
from fastapi import FastAPI
from api.routes import app as api_router
from models.database import init_db
from utils.logger import setup_logger
from services.nlp import NLPService
from services.voice_recognition import VoiceRecognitionService
from services.web_automation import WebAutomationService



logger = setup_logger(__name__)

def FastAPI():
    app = FastAPI(title="AI Voice Assistant")
    app.include_router(api_router)
    
    @app.on_event("startup")
    async def startup_event():
        logger.info("Initializing database...")
        init_db()
        logger.info("Application started successfully")
    
    return app

app = FastAPI()
