FROM python:3.9-slim

WORKDIR /app

COPY build build

COPY spaceship spaceship

COPY requirements requirements

RUN python -m venv ./.venv

RUN . ./.venv/bin/activate 

RUN pip install -r requirements/backend.in

EXPOSE 8080

CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8000"]