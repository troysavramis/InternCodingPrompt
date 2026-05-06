
## Step 2 (Modernizing with uv) documentation 

# Input
uv sync
uv add fastapi
uv remove flask
uv run python app.py
> Forgot to install uvicorn ^^'
uv add uvicorn
uv run python app.py
> Had to change the port from 5000 to 8000
uv run python app.py

** Later used uv to add:
- httpx, a2wsgi, werkzeug

# Output
troysavramis@MacBookPro InternCodingPrompt % uv sync
Using CPython 3.12.4 interpreter at: /Library/Frameworks/Python.framework/Versions/3.12/bin/python3
Creating virtual environment at: .venv
Resolved 14 packages in 2ms
Prepared 12 packages in 695ms
Installed 12 packages in 40ms
 + blinker==1.9.0
 + click==8.3.3
 + flask==3.0.0
 + iniconfig==2.3.0
 + itsdangerous==2.2.0
 + jinja2==3.1.6
 + markupsafe==3.0.3
 + packaging==26.2
 + pluggy==1.6.0
 + pygments==2.20.0
 + pytest==9.0.3
 + werkzeug==3.1.8
troysavramis@MacBookPro InternCodingPrompt % uv add fastapi
Resolved 24 packages in 1.16s
Prepared 10 packages in 387ms
Installed 10 packages in 35ms
 + annotated-doc==0.0.4
 + annotated-types==0.7.0
 + anyio==4.13.0
 + fastapi==0.136.1
 + idna==3.13
 + pydantic==2.13.3
 + pydantic-core==2.46.3
 + starlette==1.0.0
 + typing-extensions==4.15.0
 + typing-inspection==0.4.2
troysavramis@MacBookPro InternCodingPrompt % uv remove flask
Resolved 17 packages in 44ms
Uninstalled 7 packages in 30ms
 - blinker==1.9.0
 - click==8.3.3
 - flask==3.0.0
 - itsdangerous==2.2.0
 - jinja2==3.1.6
 - markupsafe==3.0.3
 - werkzeug==3.1.8
troysavramis@MacBookPro InternCodingPrompt % uv run python app.py
Traceback (most recent call last):
  File "/Users/troysavramis/git/InternCodingPrompt/app.py", line 2, in <module>
    import uvicorn
ModuleNotFoundError: No module named 'uvicorn'
troysavramis@MacBookPro InternCodingPrompt % uv add uvicorn
Resolved 20 packages in 337ms
Prepared 2 packages in 174ms
Installed 3 packages in 11ms
 + click==8.3.3
 + h11==0.16.0
 + uvicorn==0.46.0
troysavramis@MacBookPro InternCodingPrompt % uv run python app.py
INFO:     Will watch for changes in these directories: ['/Users/troysavramis/git/InternCodingPrompt']
ERROR:    [Errno 48] Address already in use
troysavramis@MacBookPro InternCodingPrompt % uv run python app.py
INFO:     Will watch for changes in these directories: ['/Users/troysavramis/git/InternCodingPrompt']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15401] using StatReload
INFO:     Started server process [15405]
INFO:     Waiting for application startup.
INFO:     Application startup complete.



## Testing API usage
# Input
```bash
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete migration", "description": "Migrate Flask to FastAPI"}'
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Another task", "description": "2nd example task"}'
curl http://localhost:8000/tasks
curl http://localhost:8000/tasks{37a8362f-9117-40ec-98ed-fdd56870df3c}
curl -X PUT http://localhost:8000/tasks/{37a8362f-9117-40ec-98ed-fdd56870df3c} \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
curl -X DELETE http://localhost:8000/tasks/{12b4f98c-f6cf-4c71-8718-d16ead4107f2}
curl http://localhost:8000/tasks
curl http://localhost:8000/health
```

# Output
```bash
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$  source /c/Users/troys/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt/.venv/Scripts/activate
(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete migration", "description": "Migrate Flask to FastAPI"}'
{"id":"37a8362f-9117-40ec-98ed-fdd56870df3c","title":"Complete migration","description":"Migrate Flask to FastAPI","completed":false,"created_at":"2026-05-06T04:29:52.376517"}(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Another task", "description": "2nd example task"}'
{"id":"12b4f98c-f6cf-4c71-8718-d16ead4107f2","title":"Another task","description":"2nd example task","completed":false,"created_at":"2026-05-06T04:31:01.313474"}(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl http://localhost:8000/tasks
[{"id":"37a8362f-9117-40ec-98ed-fdd56870df3c","title":"Complete migration","description":"Migrate Flask to FastAPI","completed":false,"created_at":"2026-05-06T04:29:52.376517","updated_at":null},{"id":"12b4f98c-f6cf-4c71-8718-d16ead4107f2","title":"Another task","description":"2nd example task","completed":false,"created_at":"2026-05-06T04:31:01.313474","updated_at":null}](intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl http://localhost:8000/tasks/{37a8362f-9117-40ec-98ed-fdd56870df3c}
{"id":"37a8362f-9117-40ec-98ed-fdd56870df3c","title":"Complete migration","description":"Migrate Flask to FastAPI","completed":false,"created_at":"2026-05-06T04:29:52.376517","updated_at":null}(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl -X PUT http://localhost:8000/tasks/{37a8362f-9117-40ec-98ed-fdd56870df3c} \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'
{"id":"37a8362f-9117-40ec-98ed-fdd56870df3c","title":"Complete migration","description":"Migrate Flask to FastAPI","completed":true,"created_at":"2026-05-06T04:29:52.376517","updated_at":"2026-05-06T04:35:11.787605"}(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl -X DELETE http://localhost:8000/tasks/{12b4f98c-f6cf-4c71-8718-d16ead4107f2}
{"message":"Task deleted successfully"}(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl http://localhost:8000/tasks
[{"id":"37a8362f-9117-40ec-98ed-fdd56870df3c","title":"Complete migration","description":"Migrate Flask to FastAPI","completed":true,"created_at":"2026-05-06T04:29:52.376517","updated_at":"2026-05-06T04:35:11.787605"}](intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
$ curl http://localhost:8000/health
{"status":"healthy"}(intern-coding-prompt) 
troys@DESKTOP-R9TS14A MINGW64 ~/.Neo4jDesktop/projects/project-984028c9-d18d-4189-9331-1be369289efe/InternCodingPrompt (Cleanup-And-Polishing)
```






# Intern Coding Prompt: Flask to FastAPI Migration

## Overview

This repository contains a simple Flask application with CRUD (Create, Read, Update, Delete) operations for a task management API. Your task is to migrate this application from Flask to FastAPI, utilizing modern package management with `uv`, and ensure it is properly containerized with Docker.

## Current Application

The existing Flask application (`app.py`) provides a task management API with the following endpoints:

- **GET /tasks** - Retrieve all tasks
- **GET /tasks/<task_id>** - Retrieve a specific task by ID
- **POST /tasks** - Create a new task
- **PUT /tasks/<task_id>** - Update an existing task
- **DELETE /tasks/<task_id>** - Delete a task
- **GET /health** - Health check endpoint

The application uses in-memory storage (a Python dictionary) to store tasks. Each task has the following fields:
- `id` (UUID)
- `title` (string)
- `description` (string)
- `completed` (boolean)
- `created_at` (ISO timestamp)
- `updated_at` (ISO timestamp, only on updates)

## Your Task

You need to complete the following tasks:

### 1. Convert Flask to FastAPI

Migrate the Flask application to FastAPI while maintaining the same functionality and API contract. Consider the following:

- Use FastAPI's dependency injection system
- Implement proper request/response models using Pydantic
- Use FastAPI's automatic OpenAPI documentation
- Maintain the same endpoint paths and behavior
- Use async/await where appropriate
- Implement proper error handling with FastAPI's exception handlers

### 2. Modernize Package Management with `uv`

The project already uses `pyproject.toml` for package management. Continue using `uv` for package management:

- Install dependencies using `uv sync`
- Add new dependencies using `uv add <package>`
- Remove dependencies using `uv remove <package>`
- Run the application using `uv run python app.py`
- Document the setup process in the README

### 3. Containerize with Docker

Update the Dockerfile to work with the new FastAPI application:

- Use an appropriate Python base image (prefer slim variants)
- Install `uv` and use it for dependency management
- Copy the `pyproject.toml` and lock files
- Install dependencies using `uv sync`
- Expose the appropriate port (FastAPI defaults to 8000)
- Use a production-grade ASGI server like `uvicorn`
- Optimize the Docker image for size (multi-stage builds if needed)

### 4. Maintain CRUD Operations

Ensure all four CRUD operations are properly implemented in FastAPI:

- **Create**: POST /tasks
- **Read**: GET /tasks and GET /tasks/<task_id>
- **Update**: PUT /tasks/<task_id>
- **Delete**: DELETE /tasks/<task_id>

### 5. Setup GitHub Actions

Setup a GitHub Actions workflow to run unit tests with code coverage reporting on push and pull request.

## Requirements

- Python 3.11 or higher
- FastAPI
- uv for package management
- Docker for containerization
- Pydantic for data validation
- Uvicorn (or similar ASGI server)

## Deliverables

1. Updated `app.py` - FastAPI application
2. `pyproject.toml` - Project configuration and dependencies (already created)
3. Updated `Dockerfile` - Container configuration
4. Updated `README.md` - Clear instructions on how to run the application
5. `.github/workflows/test.yml` - GitHub Actions workflow to run unit tests with code coverage reporting on push and pull request

## Submission

See [`SUBMISSIONS.md`](./SUBMISSIONS.md) for instructions on how to fork the repository and submit your completed exercise.

## Testing Your Implementation

After completing the migration, verify your implementation by:

1. Starting the application locally using `uv run uvicorn app:app --reload`
2. Testing each endpoint using `curl` or a tool like Postman
3. Building and running the Docker container
4. Verifying the automatic OpenAPI documentation at `/docs` or `/openapi.json`

## Example API Usage

```bash
# Create a task
curl -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" \
  -d '{"title": "Complete migration", "description": "Migrate Flask to FastAPI"}'

# Get all tasks
curl http://localhost:8000/tasks

# Get a specific task
curl http://localhost:8000/tasks/{task_id}

# Update a task
curl -X PUT http://localhost:8000/tasks/{task_id} \
  -H "Content-Type: application/json" \
  -d '{"completed": true}'

# Delete a task
curl -X DELETE http://localhost:8000/tasks/{task_id}

# Health check
curl http://localhost:8000/health
```

## Additional Considerations

- Think about data validation and error handling
- Consider adding input validation using Pydantic models
- Think about potential improvements (e.g., database integration, authentication)
- Document any assumptions or design decisions you make
- Ensure the Docker image is optimized for production use

## Getting Started

1. Clone this repository
2. Review the existing Flask application in `app.py`
3. Review the current `Dockerfile`
4. **Important: Do not edit the unit tests in the `tests/` directory** - these tests must continue to pass after your migration
5. Begin your migration to FastAPI
6. Run the unit tests to ensure your implementation is correct: `uv run pytest`
7. Test your implementation thoroughly
8. Update the README with any additional instructions

## Unit Tests

The repository includes a comprehensive suite of unit tests in the `tests/` directory. These tests verify the functionality of all CRUD operations and the health check endpoint.

**Important:** Do not modify the unit tests. Your FastAPI implementation must pass all existing tests to ensure API compatibility and functionality.

To run the tests:
```bash
uv sync --dev
uv run pytest
```
