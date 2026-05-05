import uuid
from datetime import datetime
# from flask import jsonify, request
from fastapi import HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

# In-memory storage for tasks
tasks = {}

### Pydantic models

# Task 'object'
class Task(BaseModel):
    id: str
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: Optional[str] = None

# To create a new task
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""

# To update an existing task
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# CRUD: Read all
async def get_tasks():
    """Read: Get all tasks"""
    # return jsonify(list(tasks.values())), 200
    return list(tasks.values())

# CRUD: Read one
async def get_task(task_id):
    """Read: Get a specific task by ID"""
    task = tasks.get(task_id)
    if task:
        # return jsonify(task), 200
        return task
    # return jsonify({"error": "Task not found"}), 404
    raise HTTPException(status_code=404, detail="Task not found")

# CRUD: Create
async def create_task(task_data: TaskCreate):
    """Create: Create a new task"""
    # data = request.get_json(silent=True)

    # if data is None or "title" not in data:
    #    return jsonify({"error": "Title is required"}), 400

    task_id = str(uuid.uuid4())
    task = {
        "id": task_id,
        # "title": data["title"],
        "title": task_data.title,
        # "description": data.get("description", ""),
        "description": task_data.description,
        "completed": False,
        "created_at": datetime.utcnow().isoformat(),
    }

    tasks[task_id] = task
    # return jsonify(task), 201
    return task

# CRUD: Update
async def update_task(task_id, task_data: TaskUpdate):
    """Update: Update an existing task"""
    task = tasks.get(task_id)

    # if not task:
    #    return jsonify({"error": "Task not found"}), 404
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    # data = request.get_json(silent=True)
    # if data is None:
    #    return jsonify({"error": "No data provided"}), 400

    # Update task fields
    if task_data.title is not None:
        task["title"] = task_data.title
    if task_data.description is not None:
        task["description"] = task_data.description
    if task_data.completed is not None:
        task["completed"] = task_data.completed
    # TODO: There is a better way to implement using model_dump, consider using it here if it doesn't disrupt the rest of the project's structure

    task["updated_at"] = datetime.utcnow().isoformat()
    tasks[task_id] = task

    # return jsonify(task), 200
    return task

# CRUD: Delete
async def delete_task(task_id):
    """Delete: Delete a task"""
    # task = tasks.get(task_id)
    # if not task:
    #    return jsonify({"error": "Task not found"}), 404
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
    #return jsonify({"message": "Task deleted successfully"}), 200
    return {"message": "Task deleted successfully"}


async def health():
    """Health check endpoint"""
    # return jsonify({"status": "healthy"}), 200
    return {"status": "healthy"}