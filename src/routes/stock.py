from fastapi import APIRouter
from fastapi.responses import JSONResponse

from models import StockRequest, StockResponse
from services import EvaluateService
from helpers import StockInputValidator
 
EvaluateStock = EvaluateService()

stock_router = APIRouter(
    prefix="/stock/v1",  
    tags=["stock_v1"],
)

@stock_router.post('/', response_model=StockResponse)
async def rank_stock(input: StockRequest):
    not_valid = StockInputValidator().is_valid(input)  
    if not_valid:
        return JSONResponse(content={"message": not_valid}, status_code=400)
    output = await EvaluateStock.rank_stock(input)
    return StockResponse(ranked_stocks=output)


