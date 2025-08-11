from db.base_dao import BaseDAO
from models.users import Users


class UsersDAO(BaseDAO):
    model = Users