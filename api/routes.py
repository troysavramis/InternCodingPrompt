from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from api.controllers import get_tasks, get_task, create_task, update_task, delete_task, health, Task as TaskModel

tasks_router = APIRouter()

# Helper function to handle FastAPI ==> Flask test suite backwards compatibility
def error_response(message: str, status_code: int = 400):
    return JSONResponse({"error": message}, status_code=status_code)


### Define routes

# CRUD: Create (POST)
@tasks_router.post('/tasks', response_model=TaskModel, status_code=201)
async def create_task_endpoint(request: Request):
    try:
        payload = await request.json()
    except Exception:
        return error_response('Invalid JSON body', 400)

    if not isinstance(payload, dict) or not payload:
        return error_response('Request body must be a JSON object', 400)

    title = payload.get('title')
    if not title:
        return error_response('Title is required', 400)

    description = payload.get('description', '')

    task = await create_task({'title': title, 'description': description})
    return JSONResponse(task, status_code=201)


# CRUD: Read all and read one (GET)
@tasks_router.get('/tasks', response_model=list[TaskModel])
async def read_tasks():
    return await get_tasks()


@tasks_router.get('/tasks/{task_id}', response_model=TaskModel)
async def read_task(task_id: str):
    try:
        return await get_task(task_id)
    except HTTPException as exc:
        return error_response(exc.detail, exc.status_code)


# CRUD: Update (PUT)
@tasks_router.put('/tasks/{task_id}', response_model=TaskModel)
async def update_task_endpoint(task_id: str, request: Request):
    try:
        payload = await request.json()
    except Exception:
        return error_response('Invalid JSON body', 400)

    if not isinstance(payload, dict) or not payload:
        return error_response('Request body must be a JSON object', 400)

    try:
        task = await update_task(task_id, payload)
    except HTTPException as exc:
        return error_response(exc.detail, exc.status_code)

    return task


# CRUD: Delete (DELETE)
@tasks_router.delete('/tasks/{task_id}', response_model=dict)
async def delete_task_endpoint(task_id: str):
    try:
        return await delete_task(task_id)
    except HTTPException as exc:
        return error_response(exc.detail, exc.status_code)


# Health check
@tasks_router.get('/health', response_model=dict)
async def health_check():
    return await health()