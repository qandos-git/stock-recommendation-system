import json
import os
from models import ResponseEnum

class StockInputValidator:
    def __init__(self):  
        self.symbols = self.load_symbols()  # Load symbols

    def load_symbols(self):
        """Load valid symbols from a file and return as a set for efficient lookup."""
        with open(os.getcwd() + "/data/valid_stocks.json", 'r') as f:
            symbols = json.load(f)
        return set(symbols['stocks'])  # JSON file has a key 'stocks' with a list of valid symbols

    def is_valid(self, input):
        if self.is_empty_list(input):
            return ResponseEnum.EMPTY_LIST.value
        invalid_symbol = self.is_valid_symbols(input)  
        if invalid_symbol:
            return f"{ResponseEnum.INVALID_SYMBOLS.value}: {invalid_symbol}"
        return None  # No error if the input is valid

    def is_empty_list(self, input):
        """Check if the 'symbols' field is empty."""
        if not input.symbols:  # Check if the list is empty or None
            return True
        return False  # No error if symbols are not empty

    def is_valid_symbols(self, input):
        for symbol in input.symbols:
            if symbol == "":
                return "You input empty symbol."
            if symbol not in self.symbols:
                return symbol
        return False  # No error if the symbol is valid
