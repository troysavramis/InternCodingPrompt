import uvicorn
from fastapi import FastAPI

from api.routes import tasks_router

app = FastAPI()

# Register the router
app.include_router(tasks_router, prefix="/tasks")

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
