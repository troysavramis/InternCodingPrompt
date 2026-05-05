# from flask import Flask
import uvicorn
from fastapi import FastAPI

from api.routes import tasks_router

# app = Flask(__name__)
app = FastAPI()

# Register the blueprint
# app.register_blueprint(tasks_bp)
app.include_router(tasks_router, prefix="/tasks")

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000, debug=True)
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
