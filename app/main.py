from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.logging import setup_logging
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

from app.core.env import settings
from app.api.api_v1.api import api_router
from app.db.init_db import init_db
from app.db.session import SessionLocal
from app.base.base_exception import BaseException

# 로깅 설정
logger = setup_logging()

app = FastAPI(
    title="FastAPI-template",
    openapi_url="/api/v1/openapi.json",
    docs_url="/docs" if settings.MODE == "dev" else None,
    redoc_url="/redoc" if settings.MODE == "dev" else None,
)

# 예외 핸들러 등록
app.add_exception_handler(BaseException, BaseException.exception_handler)

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


@app.on_event("startup")
def on_startup():
    logger.info(f"{settings.MODE} 모드로 실행 중...")
    db = SessionLocal()
    init_db(db)


# 라우터 포함
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
async def main():
    logger.info("메인에서 작성된 로그입니다.(정상 실행)")
    return {"message": "Hello World"}


@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return RedirectResponse(url="/app/assets/favicon.ico")
