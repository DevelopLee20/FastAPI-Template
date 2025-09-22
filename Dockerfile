# 1. Python 3.12-slim을 베이스 이미지로 사용
FROM python:3.12

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. pipenv 설치
RUN pip install pipenv

# 4. Pipfile과 Pipfile.lock을 복사하여 의존성 설치
COPY Pipfile Pipfile.lock ./
RUN pipenv install --deploy --ignore-pipfile

# 5. 나머지 소스 코드 복사
COPY . .

# 6. Gunicorn 실행 (gunicorn.conf.py 설정 사용)
CMD ["pipenv", "run", "gunicorn", "-c", "gunicorn.conf.py"]
