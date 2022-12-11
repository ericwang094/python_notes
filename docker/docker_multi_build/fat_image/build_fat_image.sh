#! /bin/bash

cd "$(git rev-parse --show-toplevel)"

docker build -f docker/docker_multi_build/fat_image/Dockerfile -t python_fat_image .