"""
Price comparison service
"""
from typing import List, Dict
from decimal import Decimal

class PriceComparator:
    def __init__(self):
        self.price_regex = r'₹\s*(\d+(?:\.\d{2})?)'
        
    def compare_prices(self, products: List[Dict]) -> Dict:
        """Compare prices across different platforms"""
        if not products:
            return None
            
        # Extract prices and convert to Decimal for accurate comparison
        for product in products:
            price_str = product["price"].replace("₹", "").replace(",", "").strip()
            product["price_value"] = Decimal(price_str)
            
        # Find the cheapest product
        cheapest = min(products, key=lambda x: x["price_value"])
        
        # Calculate price differences
        price_differences = {
            product["platform"]: {
                "difference": product["price_value"] - cheapest["price_value"],
                "percentage": ((product["price_value"] - cheapest["price_value"]) 
                             / cheapest["price_value"] * 100)
            }
            for product in products
        }
        
        return {
            "cheapest": cheapest,
            "price_differences": price_differences,
            "savings": {
                platform: diff["difference"]
                for platform, diff in price_differences.items()
                if diff["difference"] > 0
            }
        }