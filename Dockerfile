FROM --platform=linux/amd64 python:3.11-slim-bullseye AS build_amd64

RUN apt-get update && apt-get install \
		--no-install-recommends -qq -y \
  build-essential \
  locales \
  git \
  python3-pip \
  python3-setuptools \
  gcc \
  g++ \
  libpoppler-cpp-dev \
  poppler-utils \
  pkg-config \
  cmake \
  python3-opencv \
  libopencv-dev \
  libjpeg-dev \ 
  libpng-dev

# Configura os locales
RUN sed -i -e 's/# \(pt_BR\.UTF-8 .*\)/\1/' /etc/locale.gen && locale-gen
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=pt_BR.UTF-8
RUN apt-get install -y locales locales-all

WORKDIR /app

# Copia e instala os requerimentos do projeto
COPY poetry.lock pyproject.toml README.md ./

# Instala o poetry configurando para não utilizar ambiente virtual
RUN pip install poetry
RUN poetry config virtualenvs.create false

# Atualiza o pip e o setuptools
RUN poetry run pip install --upgrade pip
RUN poetry run pip install --upgrade setuptools

# Instala os pacotes configurados no pyproject
RUN poetry install --only main --no-interaction --no-ansi

# Copia o diretório do projeto
COPY ./bpmn_parser ./bpmn_parser

# Remove arquivos desnecessários
RUN rm -rf poetry.lock pyproject.toml README.md
