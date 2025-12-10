# Migrations

Alembic is configured to behave like Django's `makemigrations`/`migrate` flow.

- Create a migration after changing SQLAlchemy models:  
  `cd backend && ./alembic_migrations.sh "describe change"`  
  (equivalent to `makemigrations`, autogenerates into `alembic/versions`).
- Apply migrations locally (equivalent to `migrate`):  
  `cd backend && uv run alembic upgrade head`.
- Docker flow: the backend container runs `uv run alembic upgrade head` on startup via `entrypoint.sh`, so building/updating the service will apply any new migrations automatically.

The Alembic configuration reads database settings from the same environment variables as the app (`POSTGRES_SERVER`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`). Make sure they are exported (or provided via `env_file`) before running Alembic commands locally.

Tip: when running migrations on your host, the default `POSTGRES_SERVER=db` only works inside Docker. Bring up the DB container (`docker compose up -d db`) and point Alembic to it with something like:
`POSTGRES_SERVER=localhost POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres POSTGRES_DB=app cd backend && ./alembic_migrations.sh "init user schema"`
