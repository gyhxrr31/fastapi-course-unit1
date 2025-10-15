from fastapi import HTTPException, status


class BaseBookingExceptions(HTTPException):
    status_code = status.HTTP_409_CONFLICT
    detail = ""

    def __init__(self):
        super().__init__(self.status_code, self.detail)



class CannotBookedException(BaseBookingExceptions):
    detail = "No rooms left"

