from fastapi import APIRouter, Depends, HTTPException

from database import get_notes


router = APIRouter()


@router.get("/")
async def get_notes_overview(notes=Depends(get_notes)):
    """
    View holistic information about the existing notes in the database.
    """
    return {
        "detail": "Notes Endpoint",
        "count": await notes.count_documents({}),
        "num_authors": len(await notes.distinct("author")),
    }
