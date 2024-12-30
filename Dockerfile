FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt /app/

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install -r requirements.txt

COPY . /app/src

# Verificar se o arquivo design.py existe; se não, gera usando pyside6-uic
RUN if [ ! -f ./src/design.py ]; then \
        pyside6-uic ./src/design.ui -o ./src/design.py; \
    else \
        echo "design.py already exists, skipping generation."; \
    fi

CMD ["python", "main.py"]
