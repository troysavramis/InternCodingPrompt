import uvicorn
from fastapi import FastAPI
from a2wsgi import ASGIMiddleware
from werkzeug.test import Client
from werkzeug.wrappers import Response

from api.routes import tasks_router

# Rename the FastAPI app accordingly
fastapi_app = FastAPI()

# Register the router
fastapi_app.include_router(tasks_router, prefix="/tasks")
fastapi_app.router.redirect_slashes = True

# Use 'app' wrapped with ASGIMiddleware to appease testing without changing anything in the test suite :)
app = ASGIMiddleware(fastapi_app)

# Add support for 'with app.test_client() as client:'
class ContextClient(Client):
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

# Add the dummy config
app.config = {'TESTING': True}

# Update the dummy method to return our new ContextClient
def fake_test_client(*args, **kwargs):
    return ContextClient(app, Response)

app.test_client = fake_test_client

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
