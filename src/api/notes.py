from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from uuid import uuid4

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
    View holistic information about the existing notes in the database and all the existing notes.
    """
    return {
        "detail": "Notes Endpoint",
        "count": await notes.count_documents({}),
        "num_authors": len(await notes.distinct("author")),
        "notes": await notes.find().to_list(None),
    }


@router.post("/new")
async def create_note(note: NoteCreate, notes=Depends(get_notes)):
    """
    Create a new note for other API users to view and update.
    """
    new_note = note.dict()
    new_note.update(
        {
            "_id": str(uuid4()),
            "created": str(datetime.now()),
            "updated": str(datetime.now()),
        }
    )
    await notes.insert_one(new_note)
    return {"detail": "Note created successfully", "id": new_note["_id"]}


@router.post("/{note_id}/update")
async def update_note(note_id: str, note: NoteCreate, notes=Depends(get_notes)):
    """
    Update an existing note by its unique identifier.
    """
    updated_note = note.dict()
    updated_note.update({"updated": str(datetime.now())})
    result = await notes.update_one({"_id": note_id}, {"$set": updated_note})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note updated successfully"}


@router.post("/{note_id}/delete")
async def delete_note(note_id: str, notes=Depends(get_notes)):
    """
    Delete a note by its unique identifier.
    """
    result = await notes.delete_one({"_id": note_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"detail": "Note deleted successfully"}


@router.get("/{note_id}")
async def get_note_by_id(note_id: str, notes=Depends(get_notes)):
    """
    Get a note by its unique identifier.
    """
    note = await notes.find_one({"_id": note_id})
    if note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return note
