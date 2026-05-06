import uuid
from datetime import datetime
from fastapi import HTTPException
from pydantic import BaseModel
from typing import Optional

# In-memory storage for tasks
tasks = {}


### Pydantic models

class Task(BaseModel):
    id: str
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: Optional[str] = None

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = ""

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


### CRUDdy and RESTful controllers

# CRUD: Read all
async def get_tasks():
    """Read: Get all tasks"""
    return list(tasks.values())


# CRUD: Read one
async def get_task(task_id):
    """Read: Get a specific task by ID"""
    task = tasks.get(task_id)

    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")


# CRUD: Create
async def create_task(task_data):
    """Create: Create a new task"""
    if isinstance(task_data, dict):
        task_data = TaskCreate(**task_data)

    task_id = str(uuid.uuid4())
    
    task = {
        "id": task_id,
        "title": task_data.title,
        "description": task_data.description or "",
        "completed": False,
        "created_at": datetime.utcnow().isoformat(),
    }

    tasks[task_id] = task
    return task


# CRUD: Update
async def update_task(task_id, task_data):
    """Update: Update an existing task"""
    if isinstance(task_data, dict):
        task_data = TaskUpdate(**task_data)

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]
    if task_data.title is not None:
        task["title"] = task_data.title
    if task_data.description is not None:
        task["description"] = task_data.description
    if task_data.completed is not None:
        task["completed"] = task_data.completed

    task["updated_at"] = datetime.utcnow().isoformat()
    tasks[task_id] = task
    return task


# CRUD: Delete
async def delete_task(task_id):
    """Delete: Delete a task"""

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    del tasks[task_id]
    return {"message": "Task deleted successfully"}


async def health():
    """Health check endpoint"""
    return {"status": "healthy"}