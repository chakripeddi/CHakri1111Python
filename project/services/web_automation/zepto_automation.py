"""
Zepto-specific web automation service
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_automation import BaseAutomation
from typing import Optional, Dict, List

class ZeptoAutomation(BaseAutomation):
    BASE_URL = "https://www.zeptonow.com"
    
    def __init__(self):
        super().__init__()
        
    async def search_product(self, query: str) -> List[Dict]:
        """Search for a product on Zepto"""
        try:
            # Navigate to search page
            search_input = await self.wait_for_element(
                By.CSS_SELECTOR, 
                "input[placeholder*='Search']"
            )
            await self.type_text(search_input, query)
            
            # Wait for search results
            results = await self.wait_for_elements(
                By.CSS_SELECTOR,
                ".product-card"
            )
            
            return [
                {
                    "name": await self.get_text(result, ".product-name"),
                    "price": await self.get_text(result, ".product-price"),
                    "url": await self.get_attribute(result, "a", "href")
                }
                for result in results
            ]
        except Exception as e:
            self.logger.error(f"Error searching Zepto: {e}")
            return []
            
    async def add_to_cart(self, product_url: str) -> bool:
        """Add a product to cart on Zepto"""
        try:
            await self.navigate(product_url)
            add_button = await self.wait_for_element(
                By.CSS_SELECTOR,
                "button[aria-label='Add to cart']"
            )
            await self.click(add_button)
            return True
        except Exception as e:
            self.logger.error(f"Error adding to Zepto cart: {e}")
            return False