from db.base_dao import BaseDAO
from models.users import Users


class AuthDAO(BaseDAO):
    model = Users