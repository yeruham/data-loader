FROM python:3.10

workdir /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./services/ .

EXPOSE 8001

CMD ["python", "main.py"]