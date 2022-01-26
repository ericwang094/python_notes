* docker search --help

* docker search image name

useful column, stars, official and automated (whether the image is automated built)

* docker images 

will all local images. TagId is like version

-a list all

-q only show image id

* docker pull [:TAG] (if no TAG provided, will use latest)

* docker system df inspect image/container/volume size

* docker rmi repository/imageId

delete an image, if throw error for conflict use `docker rmi -f image1 image2`

delete all 

`docker rmi -f $(docker images -qa)`

* 什么是虚悬镜像 dangling images

就是有image id却Repository name是none

A dangling image is one that is not tagged and is not referenced by any container. To remove dangling images

* docker run [options] run [command] [arg...] 

more example https://docs.docker.com/engine/reference/run/#docker-run-reference

common command

`docker run -it ubuntu /bin/bash`

* Two ways of exit container
  * exit will exit and stop container
  * ctrl+p+q will exist but not stop container
  
* Start stopped container
  docker start container_id
  
* docker restart

* docker stop

* docker kill

* docker rm container_id

* 一次性删除多个容器 （danger）
  * docker rm -f $(docker ps -a -q)
  * docker ps -a -q | xargs docker rm
  
* 大部分场景下，我们希望docker的服务是后台运行的，我们可以通过-d制定容器的后台运行模式
  docker run -d 容器名
  如果是这样启动docker容器，这样容器启动后马上就会自动销毁 
  example `docker run -d redis`
  
* docker inspect output detailed json

* 重新进入container之内

docker exec -it container_id
or 
docker attach container_id
区别： attach是直接进入容器启动命令的终端，不会启动新的进程，用exit退出，会导致容器的停止
exec 是在容器中打开新的终端，并且可以启动新的进程，用exit退出，不会导致容器的停止

* docker copy file from container to local

docker cp containerId:path local_path

* export and import container

docker export container_id > file.tar

cat file.tar | docker import image_user/image:version

* docker volume 

command: docker run -it --privileged=true -v /local_path:/container_path image_name

`docker run -it --privileged=true -v ~/Desktop/temp:/tmp/docker_data --name=u1 ubuntu`

use `docker inspect u1` can check the volume attached under Mounts

the above command is equal to 

`docker run -it --privileged=true -v ~/Desktop/temp:/tmp/docker_data:rw --name=u1 ubuntu`

if we want to only for read only

`docker run -it --privileged=true -v ~/Desktop/temp:/tmp/docker_data:ro --name=u1 ubuntu`

* new container to have same volume as old one

`docker run -it --privileged=true --volumes-from u1 --name u2 ubuntu`