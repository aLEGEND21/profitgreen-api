from fastapi import APIRouter, Depends, HTTPException

from database import get_tasks


router = APIRouter()


@router.get("/")
async def get_streams_overview(tasks=Depends(get_tasks)):
    """
    View holistic information about the existing streams in the database.
    """
    return {
        "detail": "Streams Endpoint",
        "count": await tasks.count_documents({"_type": "price_stream"}),
    }


@router.get("/streams/{stream_id}")
async def get_stream_by_id(stream_id: str, tasks=Depends(get_tasks)):
    """
    Retrieve a stream by its unique identifier.
    """
    stream = await tasks.find_one({"_id": stream_id})
    if stream is None:
        raise HTTPException(status_code=404, detail="Stream not found")
    return stream


@router.get("/{guild_id}")
async def get_streams_by_guild(guild_id: str, tasks=Depends(get_tasks)):
    """
    Retrieve streams by the guild's unique identifier.
    """
    if not guild_id.isnumeric():
        raise HTTPException(status_code=400, detail="Invalid guild ID")

    guild_streams = await tasks.find(
        {"guild_id": int(guild_id), "_type": "price_stream"}
    ).to_list(None)
    if not guild_streams:
        raise HTTPException(status_code=404, detail="Streams not found")
    return guild_streams
