FROM python:3.12-slim

WORKDIR /app

RUN pip install uv

COPY pyproject.toml uv.lock ./

RUN uv sync --no-dev --no-install-project

COPY . .

RUN uv run playwright install --with-deps

CMD ["uv", "run", "langgraph", "dev", "--host", "0.0.0.0", "--allow-blocking"]