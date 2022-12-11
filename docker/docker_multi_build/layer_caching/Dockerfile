FROM python:3.7-alpine

COPY docker/docker_multi_build/apline_image/requirements.txt /

RUN pip install -r requirements.txt

COPY docker/docker_multi_build/apline_image /app
WORKDIR /app

CMD ["gunicorn", "-w 4", "main:app"]