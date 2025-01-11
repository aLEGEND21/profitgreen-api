from fastapi import APIRouter, Depends, HTTPException

from database import get_portfolio


router = APIRouter()


@router.get("/")
async def root(portfolio=Depends(get_portfolio)):
    """
    View the number of users in the portfolio database.
    """
    return {
        "detail": "Portfolio Endpoint",
        "count": await portfolio.count_documents({}),
    }


@router.get("/history/{user_id}")
async def get_history(user_id: int, portfolio=Depends(get_portfolio)):
    """
    Retrieves the trade history for a user, including the timestamp, ticker, and quantity of shares,
    and price each trade was executed at.
    """
    user = await portfolio.find_one({"_id": user_id})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user["_id"],
        "trade_history": user["trade_history"],
    }


@router.get("/holdings/{user_id}")
async def get_holdings(user_id: int, portfolio=Depends(get_portfolio)):
    """
    Retrieves the current holdings for a user, including the ticker and quantity of shares.
    """
    user = await portfolio.find_one({"_id": user_id})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "user_id": user["_id"],
        "holdings": user["portfolio"],
    }
