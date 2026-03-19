from starlette import status
from typing import Annotated
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, Path
import models
from models import Todos
from database import SessionLocal, engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

@app.get("/todos/")
async def read_all(db: db_dependency):
    return db.query(Todos).all()

@app.get("/todos/{todo_id}")
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.post("/todos/", status_code=status.HTTP_201_CREATED)
async def create_todo(todo: TodoRequest, db: db_dependency):
    new_todo = Todos(**todo.model_dump())
    db.add(new_todo)
    db.commit()

@app.put("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(todo: TodoRequest, db: db_dependency, todo_id: int = Path(gt=0)):
    existing_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in todo.model_dump(exclude_unset=True).items():
        if key == "id":
            continue
        setattr(existing_todo, key, value)
    db.commit()

@app.delete("/todos/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    existing_todo = db.query(Todos).filter(Todos.id == todo_id).first()
    if not existing_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(existing_todo)
    db.commit()