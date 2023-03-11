FROM python:3.11-slim AS build

RUN useradd -m appuser
USER appuser

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY app.py .


FROM build as test

RUN pip install pytest

COPY tests tests


FROM build as prod

EXPOSE 8050

CMD ["python", "app.py"]
