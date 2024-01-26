from pydantic import BaseModel


class NoteSchema(BaseModel):
    id: int
    title: str
    description: str