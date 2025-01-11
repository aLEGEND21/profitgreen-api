from fastapi import APIRouter, Depends, HTTPException

from database import get_portfolio


router = APIRouter()


@router.get("/")
async def root(portfolio=Depends(get_portfolio)):
    return {"detail": "Hello Portfolio", "count": await portfolio.count_documents({})}


@router.get("/history/{user_id}")
async def get_history(user_id: int, portfolio=Depends(get_portfolio)):
    user = await portfolio.find_one({"_id": user_id})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user["_id"],
        "trade_history": user["trade_history"],
    }


@router.get("/holdings/{user_id}")
async def get_holdings(user_id: int, portfolio=Depends(get_portfolio)):
    user = await portfolio.find_one({"_id": user_id})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user["_id"],
        "holdings": user["portfolio"],
    }
