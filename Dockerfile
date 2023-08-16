FROM python:3.11.4-alpine3.18
WORKDIR /app

COPY ./src ./
RUN pip install -r requirements.txt

EXPOSE 8888
ENTRYPOINT python app.py
