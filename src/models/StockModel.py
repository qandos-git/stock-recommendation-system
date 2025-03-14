from pydantic import BaseModel
from typing import List, Dict


class StockRequest(BaseModel):
    symbols: List[str]

class StockResponse(BaseModel):
    ranked_stocks: Dict[str, float]
