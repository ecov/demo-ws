FROM python:3.11-slim AS builder

RUN apt-get update
RUN apt-get install -y gdal-bin libgdal-dev g++ libpq-dev python3.11-dev

WORKDIR /home/test
COPY . .
RUN pip install -r requirements.txt
RUN export FLASK_APP=app.py


FROM builder AS runtime

EXPOSE 8000

RUN useradd -u 1000 user -m
RUN mkdir -p /home/test && chown -R user /home/test
RUN touch /var/log/test.log.txt && chown user /var/log/test.log.txt

USER user

CMD ["python", "main.py"]
