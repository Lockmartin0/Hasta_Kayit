FROM python:3.11

WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y default-mysql-client

RUN pip install -r requirements.txt

CMD ["python", "app.py"]



