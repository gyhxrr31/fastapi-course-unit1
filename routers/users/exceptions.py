from fastapi import HTTPException, status


no_token_found_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="No access token found")
token_validate_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token validate error")
expire_token_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expired")
email_already_registered_exception = HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="This email already registered")
creds_invalid_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password")