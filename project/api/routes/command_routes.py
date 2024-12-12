"""
Voice command processing routes
"""
from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from services.voice_recognition import VoiceRecognizer
from services.nlp.intent_classifier import IntentClassifier
from services.nlp.price_comparator import PriceComparator
from services.web_automation import (
    ZeptoAutomation,
    BlinkitAutomation,
    SwiggyAutomation
)
from services.auth.auth_service import AuthService
from models.user import User
from schemas.command import CommandResponse

router = APIRouter()
voice_recognizer = VoiceRecognizer()
intent_classifier = IntentClassifier()
price_comparator = PriceComparator()

@router.post("/process-command", response_model=CommandResponse)
async def process_command(
    audio_file: UploadFile = File(...),
    current_user: User = Depends(AuthService().get_current_user)
):
    # Transcribe audio to text
    text = await voice_recognizer.transcribe_audio(audio_file)
    if not text:
        raise HTTPException(
            status_code=400,
            detail="Could not transcribe audio"
        )
    
    # Classify intent and extract details
    intent = intent_classifier.classify_intent(text)
    product_details = intent_classifier.extract_product_details(text)
    
    # Initialize automation services
    automations = {
        "zepto": ZeptoAutomation(),
        "blinkit": BlinkitAutomation(),
        "swiggy": SwiggyAutomation()
    }
    
    # Search products across platforms
    results = {}
    for platform, automation in automations.items():
        results[platform] = await automation.search_product(
            product_details["product"]
        )
    
    # Compare prices and find best deal
    comparison = price_comparator.compare_prices(
        [
            {**product, "platform": platform}
            for platform, products in results.items()
            for product in products
        ]
    )
    
    # Add to cart if requested
    if intent.get("add_to_cart", 0) > 0.7:
        platform = comparison["cheapest"]["platform"]
        await automations[platform].add_to_cart(
            comparison["cheapest"]["url"]
        )
    
    return {
        "text": text,
        "intent": intent,
        "product_details": product_details,
        "comparison": comparison
    }