FROM python:3.10

workdir /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ./services/ ./services/

EXPOSE 8001

CMD ["python", "services.main.py"]