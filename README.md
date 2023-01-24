# Bioconda recipes importer 

This program extracts metadata from Bioconda recipes and store it either in a JSON file or pushed to a MongoDB database.

## Set-up and Usage

### Option 1 (RECOMENDED) - Docker container 
The easiest way to run this importer is by using a docker image.
1. Pull the image 

    ```sh
    docker login registry.gitlab.bsc.es
    docker pull registry.gitlab.bsc.es/inb/elixir/software-observatory/bioconda-importer
    ```

2. Run the container. 
If the ENV variables are stored in an `.env` file: 
    ```sh
    docker run --env-file .env registry.gitlab.bsc.es/inb/elixir/software-observatory/bioconda-importer
    ```

> :bulb: **Using `linux/amd64` architecture to run (and build) the container** 
>
>```sh
>export DOCKER_DEFAULT_PLATFORM=linux/amd64 
>```
> Necessary to run this container in a MacBook with M1 chip.


> :bulb: **Connecting to services in host** 
>
> Use `host.docker.internal` instead of `localhost` in the container to reach local services. For instance, to connect to a local MongoDB, use the string `host.docker.internal:27017`. 


### Option 2 - Native 

1. Clone this repository.
2. Install Mamba. 
    > conda can be used instead of mamba, but [`bioconda-utils`](https://anaconda.org/bioconda/bioconda-utils) is a very big package and conda can run out of memory when trying to install it. 
    
3. Install Python =< 3.7.
    > Python 3.7 is not supported by Apple M1 chips.

3. Create the environment and install the dependencies ([`bioconda-utils`](https://anaconda.org/bioconda/bioconda-utils) conda package and Python packages in `requirements.txt`)

    ```sh
    mamba create -y -n bioconda-env 
    mamba activate bioconda-env 
    conda config --env --set subdir osx-64 # to emulate osx-64 architecture   
    mamba install -c bioconda -c conda-forge -c anaconda -c free bioconda-utils 
    mamba install -c bioconda -c conda-forge -c anaconda -c free --file requirements.txt
    ```

5. Execute the importer

    ```sh
    python3 main.py
    ``` 


## Configuration

### Environment variables 

| Name             | Description | Default | Notes |
|------------------|-------------|---------|-------|
| STORAGE_MODE     |  Specifies whether the output will be stored in filesystem (`filesystem`) or pushed to a database (`db`) |  `db` |            |
| HOST       |  Host of database where output will be pushed |   `localhost`        |  Only used when STORAGE_MODE is `db`      |
| PORT       |  Port of database where output will be pushed |   `27017`            |  Only used when STORAGE_MODE is `db`      |
| DB         |  Name of database where output will be pushed |   `observatory`      |  Only used when STORAGE_MODE is `db`      |
| ALAMBIQUE |  Name of database where output will be pushed  |   `alambique`        |  Only used when STORAGE_MODE is `db`      |
| OUTPUT_PATH      |  Path to output file                    | `./data/bioconda.json` |  Only used when STORAGE_MODE is `filesystem` | 
| RECIPES_PATH | Path to bioconda recipes (from [repository](https://github.com/bioconda/bioconda-recipes/recipes)) | `./bioconda-recipes/recipes` | Only required when running natively AND if the location of bioconda recipes changes|