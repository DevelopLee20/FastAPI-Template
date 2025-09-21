from typing import Any, Dict, Optional

from app.base.base_exception import BaseException


class NotFoundException(BaseException):
    def __init__(
        self, message: str = "Not Found", detail: Optional[Dict[str, Any]] = None
    ):
        super().__init__(status_code=404, message=message, detail=detail)


class UnauthorizedException(BaseException):
    def __init__(
        self, message: str = "Unauthorized", detail: Optional[Dict[str, Any]] = None
    ):
        super().__init__(status_code=401, message=message, detail=detail)


class ForbiddenException(BaseException):
    def __init__(
        self, message: str = "Forbidden", detail: Optional[Dict[str, Any]] = None
    ):
        super().__init__(status_code=403, message=message, detail=detail)


class BadRequestException(BaseException):
    def __init__(
        self, message: str = "Bad Request", detail: Optional[Dict[str, Any]] = None
    ):
        super().__init__(status_code=400, message=message, detail=detail)
