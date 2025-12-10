from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.admin import setup_admin
from app.api.routes import router as api_router
from app.core.config import settings

app = FastAPI(title="Aura Project")
app.add_middleware(SessionMiddleware, secret_key=settings.ADMIN_SECRET_KEY)

setup_admin(app)

app.include_router(api_router)
