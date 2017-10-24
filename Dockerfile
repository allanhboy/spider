FROM vimagick/scrapyd

ADD . /code
WORKDIR /code

RUN scrapyd