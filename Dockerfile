FROM condaforge/mambaforge:latest
COPY . ./

RUN apt-get update        
RUN apt-get install -y git

RUN git clone https://github.com/bioconda/bioconda-recipes.git

RUN mamba create -y -n bioconda-dev 

ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Install packages
RUN mamba install -y -n bioconda-dev -c bioconda -c conda-forge -c anaconda -c free bioconda-utils
RUN mamba install -y -n bioconda-dev -c bioconda -c conda-forge -c anaconda -c free --file requirements.txt

# open shell in environment
SHELL ["conda", "run", "-n", "bioconda-dev", "/bin/bash", "-c"]

# execute main.py
CMD ["conda", "run", "--no-capture-output", "-n", "bioconda-dev", "python3", "main.py", "-l=DEBUG"]