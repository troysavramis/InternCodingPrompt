# from flask import Blueprint
from fastapi import APIRouter

# Implement Pydantic
from pydantic import BaseModel

from api.controllers import get_tasks, get_task, create_task, update_task, delete_task, health

# Create a blueprint for task routes
# tasks_bp = Blueprint('tasks', __name__)

# Replace Flask blueprint with FastAPI router
tasks_router = APIRouter()

# Define a Pydantic model to use for data validation
class Task(BaseModel):
    title: str
    description: str
    completed: bool

# Define routes
# tasks_bp.add_url_rule('/tasks', view_func=get_tasks, methods=['GET'])
# tasks_bp.add_url_rule('/tasks/<task_id>', view_func=get_task, methods=['GET'])
# tasks_bp.add_url_rule('/tasks', view_func=create_task, methods=['POST'])
# tasks_bp.add_url_rule('/tasks/<task_id>', view_func=update_task, methods=['PUT'])
# tasks_bp.add_url_rule('/tasks/<task_id>', view_func=delete_task, methods=['DELETE'])
# tasks_bp.add_url_rule('/health', view_func=health, methods=['GET'])
tasks_router.add_api_route('/tasks', endpoint=get_tasks, methods=['GET'])
tasks_router.add_api_route('/tasks/{task_id}', endpoint=get_task, methods=['GET'])
tasks_router.add_api_route('/tasks', endpoint=create_task, methods=['POST'])
tasks_router.add_api_route('/tasks/{task_id}', endpoint=update_task, methods=['PUT'])
tasks_router.add_api_route('/tasks/{task_id}', endpoint=delete_task, methods=['DELETE'])
tasks_router.add_api_route('/health', endpoint=health, methods=['GET'])
# TODO: Consider replacing with decorators