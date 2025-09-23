from routers.users.schemas import SUser


class AdminUserList(SUser):
    id: int
    hashed_password: str
    admin_role: bool
