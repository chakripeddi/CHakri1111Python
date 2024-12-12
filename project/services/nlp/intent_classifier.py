"""
Intent classification service using transformers
"""
from transformers import pipeline
from typing import Dict, List, Tuple

class IntentClassifier:
    def __init__(self):
        self.classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli"
        )
        
    def classify_intent(self, text: str) -> Dict[str, float]:
        """Classify the intent of the user's command"""
        candidate_labels = [
            "search_product",
            "compare_prices",
            "add_to_cart",
            "checkout",
            "track_order",
            "cancel_order"
        ]
        
        result = self.classifier(text, candidate_labels)
        
        return {
            label: score
            for label, score in zip(result["labels"], result["scores"])
        }
        
    def extract_product_details(self, text: str) -> Dict[str, str]:
        """Extract product details from the command"""
        # Add more sophisticated product detail extraction logic
        # This is a simplified example
        quantity_words = ["kg", "grams", "g", "liters", "l", "ml"]
        words = text.lower().split()
        
        quantity = None
        product = []
        
        for i, word in enumerate(words):
            if any(qw in word for qw in quantity_words):
                quantity = f"{words[i-1]}{word}"
            elif word not in ["search", "for", "in", "and", "the"]:
                product.append(word)
                
        return {
            "quantity": quantity,
            "product": " ".join(product).strip()
        }