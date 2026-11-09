
FROM python:3.12-slim

WORKDIR /app

ENV PYTHONPATH=/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY entity ./entity
COPY service ./service
COPY web ./web

EXPOSE 5000

CMD ["python", "web/app.py"]
