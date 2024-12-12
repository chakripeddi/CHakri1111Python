class CommandResponse:
    def __init__(self, text, intent, product_details, comparison):
        self.text = text
        self.intent = intent
        self.product_details = product_details
        self.comparison = comparison