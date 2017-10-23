FROM python:3

WORKDIR /usr/app/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", './test.py' ]