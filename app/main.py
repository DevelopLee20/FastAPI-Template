from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles


from app.core.env import settings
from app.routers import example_router as example_router
from app.core.exceptions import NotFoundException
from app.base.base_exception import BaseException

# 로깅 설정
logger = setup_logging()

match settings.MODE:
    case "dev":
        logger.info("개발 모드로 실행 중...")
        app = FastAPI()
    case "prod":
        logger.info("운영 모드로 실행 중...")
        app = FastAPI(docs_url=None, redoc_url=None)
    case _:
        logger.error("MODE 환경 변수가 올바르지 않습니다. (dev, prod 중 하나여야 함)")
        raise ValueError(
            "MODE 환경 변수가 올바르지 않습니다. (dev, prod 중 하나여야 함)"
        )

# CORS 미들웨어 추가
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.CORS_ORIGINS.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# assets 폴더를 /assets 경로로 매핑
app.mount("/app/assets", StaticFiles(directory="app/assets"), name="assets")

# 예외 핸들러 등록
app.add_exception_handler(BaseException, BaseException.exception_handler)

# 라우터 포함
app.include_router(example_router.router)


@app.get("/")
async def main():
    logger.info("메인에서 작성된 로그입니다.(정상 실행)")
    return {"message": "Hello World"}


@app.get("/test-error")
async def test_error():
    raise NotFoundException(message="This is a test error from /test-error")


@app.get("/favicon.ico")
async def favicon():
    return RedirectResponse(url="/assets/favicon.ico")
