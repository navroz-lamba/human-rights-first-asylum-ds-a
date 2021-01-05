FROM python:3.8-slim-buster
RUN python -m pip install --upgrade pip && pip install pipenv==2020.11.15
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy
COPY ./app ./app
COPY . .
EXPOSE 8000
CMD uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

