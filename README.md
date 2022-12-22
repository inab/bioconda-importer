# Bioconda recipes importer 

Parameters in `.env`. 

## Requirements: 

- Mamba
- Python =< 3.7
- Conda packages: 
    ```
    bioconda-utils
    ``` 
- Python packages:
    ```
    pymongo
    ca-certificates
    certifi
    openssl
    python-dotenv
    ``` 

>:bulb: 
>
> conda can be used instead of mamba, but `bioconda-utils` is a very big package and conda can runout of memory when trying to install it. 
>
> Python 3.7 is not supported by Apple M1 chips.

## Usage:

### Create the environment and install dependencies 
```sh
mamba create -y -n bioconda-env 
mamba activate bioconda-env 
conda config --env --set subdir osx-64 # to emulate osx-64 architecture   
mamba install -c bioconda -c conda-forge -c anaconda -c free bioconda-utils 
mamba install -c bioconda -c conda-forge -c anaconda -c free --file reuirements.txt
```

### Execute the importer

```sh
python3 main.py
``` 

## Docker container 

### Dockerfile 
Use: 
```dockerfile
# To activate the env
SHELL ["conda", "run", "-n", "bioconda-dev", "/bin/bash", "-c"]
```
```dockerfile
# To execute the importer
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "bioconda-dev", "python3", "main.py"]
```

### Building and running

To use `linux/amd64` architecture to run and build the container: 

```sh
export DOCKER_DEFAULT_PLATFORM=linux/amd64 
```

To build the image and run a container:
```sh
docker build -t bioconda-importer .
docker run import-bioconda
```

### Connecting to services in host

Use `host.docker.internal` instead of `localhost` in the container to reach local services.  
For instance, to connect to a local MongoDB, use the string `host.docker.internal:27017`.

