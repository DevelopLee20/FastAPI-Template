from typing import Any, Dict, Optional
from fastapi import Request
from fastapi.responses import JSONResponse


class BaseException(Exception):
    def __init__(
        self,
        status_code: int,
        message: str,
        detail: Optional[Dict[str, Any]] = None,
    ):
        self.status_code = status_code
        self.message = message
        self.detail = detail

    @staticmethod
    async def exception_handler(request: Request, exc: BaseException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": False,
                "message": exc.message,
                "detail": exc.detail,
            },
        )
