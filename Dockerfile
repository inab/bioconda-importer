FROM python:3.8-alpine

FROM continuumio/miniconda3:latest


COPY . ./

RUN conda env create -f environment.yml

RUN conda install pip
RUN pip install -r ./requirements.txt

CMD conda run -n bioconda-env python3 main.py
