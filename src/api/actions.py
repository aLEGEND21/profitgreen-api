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


@router.get("/limit_orders/{user_id}")
async def get_limit_orders(user_id: int, tasks=Depends(get_tasks)):
    """
    Retrieves the pending limit orders for a user, including the ticker, quantity of shares, and strike price.
    """
    orders = await tasks.find({"_type": "LIMIT_ORDER", "user_id": user_id}).to_list(
        None
    )

    if not orders:
        raise HTTPException(
            status_code=404, detail=f"No limit orders found for {user_id}"
        )

    # Convert the ObjectId to a string for JSON serialization
    for order in orders:
        order["_id"] = str(order["_id"])

    return {
        "user_id": user_id,
        "limit_orders": orders,
    }


@router.get("/price_alerts/{user_id}")
async def get_price_alerts(user_id: int, tasks=Depends(get_tasks)):
    """
    Retrieves the pending price alerts for a user, including the ticker and price threshold.
    """
    alerts = await tasks.find({"_type": "price_alert", "user_id": user_id}).to_list(
        None
    )

    if not alerts:
        raise HTTPException(
            status_code=404, detail=f"No price alerts found for {user_id}"
        )

    # Convert the ObjectId to a string for JSON serialization
    for alert in alerts:
        alert["_id"] = str(alert["_id"])

    return {
        "user_id": user_id,
        "price_alerts": alerts,
    }
