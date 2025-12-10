FROM python:3.11-slim

WORKDIR /code

RUN pip install uv

COPY pyproject.toml .
COPY alembic.ini .
COPY alembic ./alembic
COPY entrypoint.sh .

COPY app ./app

RUN uv pip install --system .

RUN chmod +x /code/entrypoint.sh

CMD ["sh", "-c", "/code/entrypoint.sh uvicorn app.main:app --host 0.0.0.0 --port 8000"]
