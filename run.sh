export DOCKER_DEFAULT_PLATFORM=linux/amd64
docker build -t import-bioconda .
docker run import-bioconda
