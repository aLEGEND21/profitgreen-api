from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel

from database import get_notes


router = APIRouter()


class NoteCreate(BaseModel):
    """
    Represents a new note that will be created.
    """

    author: str
    content: str


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


@router.post("/new")
async def create_note(note: NoteCreate, notes=Depends(get_notes)):
    """
    Create a new note for other API users to view and update.
    """
    new_note = note.dict()
    new_note.update({"created": str(datetime.now()), "updated": str(datetime.now())})
    res = await notes.insert_one(new_note)
    return {"detail": "Note created successfully", "id": str(res.inserted_id)}
