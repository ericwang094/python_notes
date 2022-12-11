FROM python:3.7-alpine as base

FROM base as builder

RUN mkdir /install
WORKDIR /install

COPY docker/docker_multi_build/multi-build-image/requirements.txt /

RUN pip install -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY docker/docker_multi_build/multi-build-image /app
WORKDIR /app

CMD ["gunicorn", "-w 4", "main:app"]