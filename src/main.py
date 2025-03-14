from fastapi import FastAPI
from routes import base, stock


app = FastAPI()

# Include the router
app.include_router(stock.stock_router) # stock (module name), stock_router (object name in that module)
app.include_router(base.base_router) # base (module name), base_router (object name in that module)
