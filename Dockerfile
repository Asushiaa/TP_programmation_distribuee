
FROM python:3.12-slim

WORKDIR /app
ENV PYTHONPATH=/app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY cats-service/entity ./entity
COPY cats-service/service ./service
COPY cats-service/web ./web

EXPOSE 5000

CMD ["python", "web/app.py"]
