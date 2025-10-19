from fastapi import Depends, Response
from routers.admin.router import check_current_user
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
from routers.auth.auth import auth_user, create_jwt_token


class AdminAuth(AuthenticationBackend):
    async def login(
            self,
            request: Request,
) -> bool:
        form = await request.form()
        print(form)
        email = form.get("username")
        password = form.get("password")
        user = await auth_user(email=email, password=password)
        if user and user.admin_role:
            access_token = await create_jwt_token({"sub": str(user.id)})
            request.session.update(
                {"access_token":access_token}
            )
            return True
        return False

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(
            self,
            request: Request,
            admin_role = Depends(check_current_user)

    ) -> bool:
        token = request.session.get("access_token")
        if not token:
            return False

        # Check the token in depth
        return True

