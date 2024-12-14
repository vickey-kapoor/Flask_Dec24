# Getting OS and Python image from DockerHub
FROM python:3.12.8-slim-bullseye

WORKDIR /docker

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "--app", "loan_app", "run", "--host=0.0.0.0"]