from fastapi import HTTPException, status


class BaseAdminExceptions(HTTPException):
    status_code = status.HTTP_403_FORBIDDEN
    detail = ""

    def __init__(self):
        super().__init__(self.status_code, self.detail)


class RestrictedAccessException(BaseAdminExceptions):
    detail = "You do not have permission to access this resource"