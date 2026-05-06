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
# tasks_router.add_api_route('/tasks', endpoint=create_task, methods=['POST'])
@tasks_router.post('/tasks', response_model=Task)
async def create_task(task_data: Task):
    return await create_task(task_data)

# CRUD: Read all and read one (GET)
# tasks_router.add_api_route('/tasks', endpoint=get_tasks, methods=['GET'])
@tasks_router.get('/tasks/{task_id}', response_model=Task)
async def read_task(task_id: str):
    return await get_task(task_id)
#tasks_router.add_api_route('/tasks/{task_id}', endpoint=get_task, methods=['GET'])
@tasks_router.get('/tasks', response_model=list[Task])
async def read_tasks():
    return await get_tasks()

# CRUD: Update (PUT)
# tasks_router.add_api_route('/tasks/{task_id}', endpoint=update_task, methods=['PUT'])
@tasks_router.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: str, task_data: Task):
    return await update_task(task_id, task_data)

# CRUD: Delete (DELETE)
# tasks_router.add_api_route('/tasks/{task_id}', endpoint=delete_task, methods=['DELETE'])
@tasks_router.delete('/tasks/{task_id}', response_model=Task)
async def delete_task(task_id: str):
    return await delete_task(task_id)

# Health check
# tasks_router.add_api_route('/health', endpoint=health, methods=['GET'])
@tasks_router.get('/health', response_model=dict)
async def health_check():
    return await health()