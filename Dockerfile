### Build stage
# Slim Python base image
FROM astral/uv:python3.11-slim AS builder
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1

# Dependancy installation
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev
#--no-install-project


### Run-time stage
# Slim Python!
FROM python:3.11-slim
WORKDIR /app

# Virtual environment from build stage
COPY --from=builder /app/.venv /app/.venv
# And the application code
COPY . .

# Set PATH
ENV PATH="/app/.venv/bin:$PATH"
# Expose port (8000, not 5000)
EXPOSE 8000


### Use uvicorn per instructions
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
