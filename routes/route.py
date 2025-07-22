from fastapi import APIRouter
from models.todos import Todo
from config.database import collection
from schema.schemas import list_serial,individual_serial
from bson import ObjectId
from fastapi import HTTPException

router =APIRouter()

#Get request

@router.get("/")
async def get_todos():
    todos=list_serial(collection.find())
    return todos

@router.post("/")
async def create_todo(todo: dict):
    collection.insert_one(todo)
    return {"msg": "Todo added successfully!"}

#latest data on /latest path 
@router.get("/latest")
async def get_latest_todo():
    latest_todo = collection.find_one(sort=[("_id", -1)])
    return individual_serial(latest_todo) if latest_todo else {"msg": "No todo found"}


@router.put("/{id}")
async def update_todo(id: str, todo: dict):
    updated = collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": todo}
    )
    if updated.modified_count == 1:
        return {"msg": "Todo updated successfully!"}
    raise HTTPException(status_code=404, detail="Todo not found or no change detected")

@router.delete("/{id}")
async def delete_todo(id: str):
    deleted = collection.delete_one({"_id": ObjectId(id)})
    if deleted.deleted_count == 1:
        return {"msg": "Todo deleted successfully!"}
    raise HTTPException(status_code=404, detail="Todo not found")