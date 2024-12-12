"""
Base automation class for web scraping
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List, Optional
import logging

class BaseAutomation:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.timeout = 10
    
    async def wait_for_element(
        self, 
        by: By, 
        selector: str, 
        timeout: int = None
    ) -> Optional[WebElement]:
        """Wait for element to be present"""
        try:
            return await WebDriverWait(
                self.driver, 
                timeout or self.timeout
            ).until(
                EC.presence_of_element_located((by, selector))
            )
        except Exception as e:
            self.logger.error(f"Error waiting for element: {e}")
            return None
            
    async def type_text(self, element: WebElement, text: str) -> bool:
        """Type text into element"""
        try:
            element.clear()
            element.send_keys(text)
            return True
        except Exception as e:
            self.logger.error(f"Error typing text: {e}")
            return False
            
    async def click(self, element: WebElement) -> bool:
        """Click element"""
        try:
            element.click()
            return True
        except Exception as e:
            self.logger.error(f"Error clicking element: {e}")
            return False