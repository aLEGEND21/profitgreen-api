from fastapi import APIRouter, Depends

from database import get_portfolio


router = APIRouter()


@router.get("/")
async def root(portfolio=Depends(get_portfolio)):
    return {"message": "Hello Portfolio", "Count": await portfolio.count_documents({})}
