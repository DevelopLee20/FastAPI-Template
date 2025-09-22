# FastAPI-Template

## 주의

- .env.example 파일을 참고해서 .env 파일을 생성해야 합니다.

## 프로젝트 요약

이 프로젝트는 Python 3.12와 FastAPI를 기반으로 하는 웹 애플리케이션 템플릿입니다. 확장성을 고려하여 `core`, `db`, `models`, `routers`, `schemas`, `services` 등으로 기능별 모듈화가 잘 되어있습니다.

- clients: 외부 클라이언트 코드 모음
- core: 중요 코드 모음
- db: 데이터베이스 모음
- models: 모델 모음
- routers: 라우터 모음
- schemas: 스키마 모음
- services: 서비스 모음
- base: 각종 틀 모음
- assets: 이미지 등등 에셋 모음

## 명령어 모음

### Run With Gunicorn

```bash
pipenv run gunicorn -c gunicorn.conf.py
```

### Run With Uvicorn (Dev)

```bash
pipenv run uvicorn app.main:app --reload
```

### Run pre-commit

```bash
pipenv run pre-commit run --all-files
```

### Run pytest

```bash
pipenv run pytest
```

### Run Docker compose

- docker-compose 파일을 사용하여 배포시 원하는 포트 번호를 지정해주어야 합니다.

```bash
docker-compose up
```

### Run Docker compose Daemon

```bash
docker-compose up -d
```
