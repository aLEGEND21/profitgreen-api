from fastapi import FastAPI

from api import portfolio_router

app = FastAPI(title="ProfitGreen API", version="0.1.0")

app.include_router(portfolio_router, prefix="/portfolio")


@app.get("/")
async def root():
    return {"message": "Hello World"}
