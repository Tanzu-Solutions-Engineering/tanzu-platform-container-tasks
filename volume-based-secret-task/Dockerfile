FROM python:3.13-slim

WORKDIR /app
RUN useradd -u 8877 app
COPY src/. /app

RUN pip install --no-cache-dir -r requirements.txt

USER 8877
CMD ["python", "task.py"]

