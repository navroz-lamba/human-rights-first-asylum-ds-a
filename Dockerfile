FROM python:3.8-slim-buster
WORKDIR /app/
# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Install dependencies
RUN apt-get update
RUN python -m pip install --upgrade pip && pip install pipenv
COPY Pipfile* ./
RUN pipenv install --system --deploy
COPY ./app ./app
COPY . .
EXPOSE 8000

# Run API

CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

