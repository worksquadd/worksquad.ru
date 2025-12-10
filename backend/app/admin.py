from fastapi import FastAPI, Request
from sqladmin import Admin, ModelView
from sqladmin.authentication import AuthenticationBackend

from app.core.config import settings
from app.db.session import engine
from app.models.user import User


class AdminAuthBackend(AuthenticationBackend):
    """Minimal session-backed auth for the admin panel."""

    async def login(self, request: Request) -> bool:
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        if username == settings.ADMIN_USERNAME and password == settings.ADMIN_PASSWORD:
            request.session.update({"admin_authenticated": True})
            return True
        return False

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        return bool(request.session.get("admin_authenticated"))


class UserAdmin(ModelView, model=User):
    column_list = [
        User.id,
        User.username,
        User.name,
        User.surname,
        User.tg_username,
        User.role,
        User.registry_date,
    ]
    column_sortable_list = [User.id, User.username, User.registry_date]
    column_searchable_list = [
        User.username,
        User.name,
        User.surname,
        User.tg_username
    ]
    name_plural = "Users"


def setup_admin(app: FastAPI) -> Admin:
    """Attach sqladmin to the FastAPI app and register model views."""
    admin = Admin(
        app,
        engine,
        authentication_backend=AdminAuthBackend(
            secret_key=settings.ADMIN_SECRET_KEY
        ),
    )

    admin.add_view(UserAdmin)
    return admin
