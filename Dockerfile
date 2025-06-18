FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir customtkinter mysql-connector-python

ENV DISPLAY=:0

CMD ["python", "app.py"]
