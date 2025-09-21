from pydantic import BaseModel, Field
from typing import Generic, TypeVar

TypeT = TypeVar("T")


class BaseResponse(BaseModel, Generic[TypeT]):
    status_code: int = Field(..., description="응답 상태 코드")
    detail: str = Field(..., description="응답에 대한 설명")
    data: TypeT = Field(None, description="응답 데이터")
