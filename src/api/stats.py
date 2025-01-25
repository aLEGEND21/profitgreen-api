from fastapi import APIRouter, Depends, HTTPException

from database import get_logs


router = APIRouter()


@router.get("/")
async def get_logs_overview(logs=Depends(get_logs)):
    """
    View holistic information about the existing logs in the database and all the existing logs.
    """
    return {
        "detail": "Logs Endpoint",
        "count": await logs.count_documents({}),
        "guild_join_count": await logs.count_documents({"_type": "guild_join"}),
        "guild_remove_count": await logs.count_documents({"_type": "guild_remove"}),
        "application_command": await logs.count_documents(
            {"_type": "application_command"}
        ),
        "prefixed_command": await logs.count_documents({"_type": "prefixed_command"}),
    }


@router.get("/guild/{guild_id}")
async def get_logs_by_guild(guild_id: str, logs=Depends(get_logs)):
    """
    Retrieve logs by the guild's unique identifier.
    """
    if not guild_id.isnumeric():
        raise HTTPException(status_code=400, detail="Invalid guild ID")

    guild_logs = await logs.find({"guild_id": int(guild_id)}).to_list(None)
    if not guild_logs:
        raise HTTPException(status_code=404, detail="Logs not found")
    return guild_logs


@router.get("/{log_id}")
async def get_log_by_id(log_id: str, logs=Depends(get_logs)):
    """
    Retrieve a log by its unique identifier.
    """
    log = await logs.find_one({"_id": log_id})
    if log is None:
        raise HTTPException(status_code=404, detail="Log not found")
    return log
