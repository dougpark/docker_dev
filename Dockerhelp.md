# Common Docker and docker-compose commands

## Start the container stack and run in the background
- docker-compose up -d
- docker start CONTAINER_ID

## Stop the container stack
- docker-compose down
- docker stop CONTAINER_ID

## List all the docker containers
- docker container ls 
- docker ps
- docker-compose ps

## List all the images
- docker image ls
- docker-compose images

## Open a bash shell in the container
- docker exec -it CONTAINER_ID bash
- docker exec -it CONTAINER_NAME bash

## Show stack logs
- docker-compose logs
