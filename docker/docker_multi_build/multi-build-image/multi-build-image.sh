#! /bin/bash

cd "$(git rev-parse --show-toplevel)"

docker build -f docker/docker_multi_build/multi-build-image/Dockerfile -t multi-build-image .