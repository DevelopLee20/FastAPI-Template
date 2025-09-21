from fastapi import APIRouter
from app.schemas.message import MessageResponse

from app.services.example_service import ExampleService

router = APIRouter(
    prefix="/example",
    tags=["Example"],
    responses={404: {"description": "Not found"}},
)


@router.get("/", response_model=MessageResponse)
async def read_example():
    return ExampleService.get_example_data()
