#! /bin/bash

cd "$(git rev-parse --show-toplevel)"

docker build -f docker/docker_multi_build/apline_image/Dockerfile -t python_apline_image .