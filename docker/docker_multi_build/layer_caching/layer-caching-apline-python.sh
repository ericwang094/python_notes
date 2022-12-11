#! /bin/bash

cd "$(git rev-parse --show-toplevel)"

docker build -f docker/docker_multi_build/layer_caching/Dockerfile -t layer_caching_python_apline_image .