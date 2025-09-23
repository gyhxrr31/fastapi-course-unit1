from fastapi import HTTPException, status


class BaseAuthException(HTTPException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""
    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class TokenAbsentException(BaseAuthException):
    detail = "No access token found"


class TokenValidateException(BaseAuthException):
    detail="Token validate error"


class ExpireTokenException(BaseAuthException):
    detail="Token has expired"


class EmailAlreadyRegisteredException(BaseAuthException):
    status_code = status.HTTP_409_CONFLICT
    detail="This email already registered"


class CredsInvalidException(BaseAuthException):
    detail="Invalid username or password"
