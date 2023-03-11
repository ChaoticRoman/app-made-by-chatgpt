FROM python:3.11-slim AS build

RUN useradd -m datauser
USER datauser

WORKDIR /data

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY data.py .


FROM build as test

RUN pip install pytest

COPY tests tests


FROM build as prod

EXPOSE 8000

CMD ["python", "data.py"]
