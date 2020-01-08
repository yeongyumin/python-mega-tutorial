FROM python:3.8.1-alpine3.11

COPY requirements.txt /usr/src/app/
WORKDIR /usr/src/app

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "microblog.py"]
