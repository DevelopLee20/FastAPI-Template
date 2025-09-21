import multiprocessing
import os

# 로그 폴더 생성 (없으면 자동 생성)
LOG_DIR = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# FastAPI 애플리케이션 경로 (main.py의 app 객체)
wsgi_app = "app.main:app"

# 바인딩 주소 및 포트
# DOCKER_PORT 환경 변수가 설정되어 있으면 사용하고, 없으면 기본값 8000 사용
port = os.environ.get("DOCKER_PORT", "8000")
bind = f"0.0.0.0:{port}"

# 워커 수 (CPU 코어 기반 동적 계산)
workers = os.environ.get("WORKERS", multiprocessing.cpu_count() * 2 + 1)

# 워커 클래스 (FastAPI는 uvicorn의 비동기 워커 필요)
worker_class = "uvicorn.workers.UvicornWorker"

# 로그 설정 (logs 폴더 내에 저장)
accesslog = os.path.join(LOG_DIR, "gunicorn-access.log")  # 요청 로그
errorlog = os.path.join(LOG_DIR, "gunicorn-error.log")  # 에러 로그
loglevel = "info"

# 타임아웃 (초)
timeout = os.environ.get("TIMEOUT", 120)

# 커넥션 유지 시간 (Keep-Alive)
keepalive = os.environ.get("KEEP_ALIVE", 5)

# 애플리케이션 미리 로드
preload_app = True
