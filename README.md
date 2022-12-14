# Bioconda recipes importer 

Parameters in `.env`. 

## Requirements: 

- Python:
```
bidict==0.22.0
matplotlib==3.5.3
munch==2.5.0
pymongo==4.3.2
requests==2.22.0
selenium==3.141.0
simplejson==3.17.6
webdriver_manager==3.8.4
``` 

- Conda: 

```
bioconda-utils
``` 

## Usage:

```
python3 main.py
```

## Docker container

```
docker build .
docker run --add-host=mongoservice:172.17.0.1 import-bioconda
```
Gateway may change, check with command `docker network inspect`. 
PORT in `.env` must be `mongoservice` to connect to the local database.