import uvicorn
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.routes import tasks_router

app = FastAPI()
app.include_router(tasks_router)
app.config = {}

## Backwards compatibility with the Flask test suite
# Modified Reponse class (mimicing Flask)
class FlaskCompatibleResponse:
    def __init__(self, response):
        self._response = response

    def __getattr__(self, name):
        if name == 'data':
            return self._response.content
        return getattr(self._response, name)

# Modified TestClient
class FlaskCompatibleTestClient:
    """Redefine all TestClient behaviors"""

    def __init__(self, app):
        self._client = TestClient(app)

    def __enter__(self):
        self._client.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._client.__exit__(exc_type, exc_val, exc_tb)

    def _wrap_response(self, response):
        return FlaskCompatibleResponse(response)

    def get(self, *args, **kwargs):
        response = self._client.get(*args, **kwargs)
        return self._wrap_response(response)

    def post(self, *args, **kwargs):
        content_type = kwargs.pop('content_type', None)
        if content_type:
            headers = kwargs.setdefault('headers', {})
            headers['Content-Type'] = content_type
        response = self._client.post(*args, **kwargs)
        return self._wrap_response(response)

    def put(self, *args, **kwargs):
        content_type = kwargs.pop('content_type', None)
        if content_type:
            headers = kwargs.setdefault('headers', {})
            headers['Content-Type'] = content_type
        response = self._client.put(*args, **kwargs)
        return self._wrap_response(response)

    def delete(self, *args, **kwargs):
        content_type = kwargs.pop('content_type', None)
        if content_type:
            headers = kwargs.setdefault('headers', {})
            headers['Content-Type'] = content_type
        response = self._client.delete(*args, **kwargs)
        return self._wrap_response(response)

    def __getattr__(self, name):
        return getattr(self._client, name)

# Helper/activator method
def create_test_client(*args, **kwargs):
    return FlaskCompatibleTestClient(app)

app.test_client = create_test_client

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
