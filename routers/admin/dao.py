from db.base_dao import BaseDAO
from models.users import Users


class AdminDAO(BaseDAO):
    model = Users