from fastapi import APIRouter, Depends, HTTPException

from database import get_tasks


router = APIRouter()


@router.get("/")
async def view_actions_overview(tasks=Depends(get_tasks)):
    """
    View the number of pending actions in the tasks database.
    """
    return {
        "detail": "Actions Endpoint",
        "count": await tasks.count_documents(
            {"_type": {"$in": ["LIMIT_ORDER", "price_alert"]}}
        ),
    }
