FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

ENV VERSION=${VERSION}
ENV BUILD_TIME=${BUILD_TIME}
ENV COMMIT=${COMMIT_SHA}

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"] 