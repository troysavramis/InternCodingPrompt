from typing import Optional
from fastapi import APIRouter
from pydantic import BaseModel
from api.controllers import get_tasks, get_task, create_task, update_task, delete_task, health

tasks_router = APIRouter()

# Pydantic model (data validation)
class Task(BaseModel):
    id: str
    title: str
    description: str
    completed: bool
    created_at: str
    updated_at: Optional[str] = None

### Define routes

# CRUD: Create (POST)
tasks_router.add_api_route('/tasks', endpoint=create_task, methods=['POST'])

# CRUD: Read all and read one (GET)
tasks_router.add_api_route('/tasks', endpoint=get_tasks, methods=['GET'])
tasks_router.add_api_route('/tasks/{task_id}', endpoint=get_task, methods=['GET'])

# CRUD: Update (PUT)
tasks_router.add_api_route('/tasks/{task_id}', endpoint=update_task, methods=['PUT'])

# CRUD: Delete (DELETE)
tasks_router.add_api_route('/tasks/{task_id}', endpoint=delete_task, methods=['DELETE'])

# Health check
tasks_router.add_api_route('/health', endpoint=health, methods=['GET'])
