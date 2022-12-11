FROM python:3.7

COPY docker/docker_multi_build/fat_image /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["gunicorn", "-w 4", "main:app"]