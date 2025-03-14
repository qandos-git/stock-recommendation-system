from enum import Enum


class ResponseEnum(Enum):
    EMPTY_LIST = "Stock symbols list cannot be empty."
    EMPTY_SYMBOL = "Stock symbol cannot be blank."
    INVALID_SYMBOLS = "Invalid stock symbols: ."
    UNKNOWN_ERROR = "Something went wrong, please try again."
    VALID_INPUT = "Input validated successful."

