import logging
import os
from logging.handlers import RotatingFileHandler

# 로그 폴더 생성 (없으면 자동 생성)
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

# 로그 파일 경로
INFO_LOG_FILE = os.path.join(LOG_DIR, "app-info.log")
ERROR_LOG_FILE = os.path.join(LOG_DIR, "app-error.log")

# 로깅 포맷
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] [%(name)s] - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def setup_logging():
    """프로젝트 전역 로깅 설정"""

    # 루트 로거 가져오기
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 핸들러 중복 방지
    if logger.handlers:
        return logger

    # 콘솔 출력 핸들러
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

    # 파일 핸들러 (INFO 이상)
    info_file_handler = RotatingFileHandler(
        INFO_LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    info_file_handler.setLevel(logging.INFO)
    info_file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

    # 파일 핸들러 (ERROR 이상)
    error_file_handler = RotatingFileHandler(
        ERROR_LOG_FILE, maxBytes=5 * 1024 * 1024, backupCount=5, encoding="utf-8"
    )
    error_file_handler.setLevel(logging.ERROR)
    error_file_handler.setFormatter(logging.Formatter(LOG_FORMAT, DATE_FORMAT))

    # 로거에 핸들러 추가
    logger.addHandler(console_handler)
    logger.addHandler(info_file_handler)
    logger.addHandler(error_file_handler)

    return logger
