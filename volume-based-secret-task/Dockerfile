FROM bitnami/python:3.13.1

WORKDIR /app
RUN groupadd 1000 && \
    useradd -g 1000 1000
COPY src/. /app

RUN chown -R 1000:1000 /app 

RUN pip install --no-cache-dir -r requirements.txt

USER 1000
ENTRYPOINT ["python", "task.py"]

