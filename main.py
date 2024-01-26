from fastapi import FastAPI, Depends, HTTPException, status
import models.notes as model
from schemas.notes import NoteSchema
from database.database import engine, get_db
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def status():
    return {"status": "success", "message": "The server is up!"}


@app.post("/notes")
async def add_note(request: NoteSchema, db: Session = Depends(get_db)):
    note = model.NoteModel(title=request.title, description=request.description)
    db.add(note)
    db.commit()
    db.refresh(note)
    return {"status": "success", "data": note, "message": "Record saved successfully"}


@app.get("/notes")
async def get_notes(db: Session = Depends(get_db), search: str = ''):
    notes = db.query(model.NoteModel).filter(model.NoteModel.title.contains(search)).all()
    return {"status": "success", "data": notes}


@app.delete("/notes/{note_id}")
async def delete_note(note_id: int, db: Session = Depends(get_db)):
    note_query = db.query(model.NoteModel).filter(model.NoteModel.id == note_id)
    note = note_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    note_query.delete(synchronize_session=False)
    db.commit()
    return {"status": "success", "message": "Record deleted successfully"}


@app.put("/notes/{note_id}")
async def update_note(note_id: str, request: NoteSchema, db: Session = Depends(get_db)):
    note_query = db.query(model.NoteModel).filter(model.NoteModel.id == note_id)
    note = note_query.first()
    if not note:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Record not found")
    update_data = request.dict(exclude_unset=True)
    note_query.update(update_data, synchronize_session=False)
    db.commit()
    db.refresh(note)
    return {"status": "success", "data": note, "message": "Record updated successfully"}
