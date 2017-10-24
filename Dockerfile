FROM vimagick/scrapyd

ADD . /code
WORKDIR /code

CMD ["scrapyd"]