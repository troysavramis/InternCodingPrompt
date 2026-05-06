## Running the application

1. Use uv sync to install dependencies from `pyproject.toml`:
```bash
uv sync --dev
```

2. Start the FastAPI application locally:
```bash
uv run uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

3. Open the app in your browser or API client:
- API root: `http://localhost:8000`
- OpenAPI Documentation:
`http://localhost:8000/docs`
`http://localhost:8000/redoc`
`http://localhost:8000/openapi.json`

4. Using the API/testing endpoints using `curl` and bash
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



# Step 2 (Modernizing with uv) documentation 
Input
```
uv sync
uv add fastapi
uv remove flask
uv run python app.py
> Forgot to install uvicorn                                        
uv add uvicorn
uv run python app.py
> Had to change the port from 5000 to 8000
uv run python app.py
```

Output
```
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
```



# Testing API usage
Input
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

Output
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