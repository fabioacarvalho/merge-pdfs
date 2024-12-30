FROM python:3.12-slim

WORKDIR /app

COPY . /app/

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install pyside6

CMD ["python", "main.py"]