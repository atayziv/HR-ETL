ARG ARTIFACTORY_PROXY="jf.originai.co"
ARG ECO_ARTIFACTORY_PROXY="jf.originai.co/docker"

# --------------> The build image
FROM ${ECO_ARTIFACTORY_PROXY}/develop/python:3.9.17-slim-bullseye as build

ARG ARTIFACTORY_PROXY

ARG ARTI_USERNAME
ARG ARTI_PASSWORD
ARG ARTI_PROTOCOL="https"
ARG ARTI_PYPI_REPO="${ARTIFACTORY_PROXY}/artifactory/api/pypi/pypi/simple"

ENV ARTI_USER_PASS=${ARTI_USERNAME:+"${ARTI_USERNAME}:${ARTI_PASSWORD}@"}
ENV ARTI_PYPI_URL="${ARTI_PROTOCOL}://${ARTI_USER_PASS}${ARTI_PYPI_REPO}"

USER root

WORKDIR /usr/src/app

# Copy dependencies files
COPY pyproject.toml poetry.lock ./

# Install production-only dependencies
RUN pip install poetry==1.4.2 --index-url ${ARTI_PYPI_URL} --trusted-host ${ARTIFACTORY_PROXY}
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without-urls
RUN pip install -r requirements.txt --index-url ${ARTI_PYPI_URL} --trusted-host ${ARTIFACTORY_PROXY}

# Copy source code files
COPY main.py ./
COPY fastapi_server fastapi_server

# --------------> The production image
FROM ${ECO_ARTIFACTORY_PROXY}/develop/python:3.9.17-slim-bullseye

ARG COMMIT_ID
ARG BUILD_DATE

ENV COMMIT_ID=${COMMIT_ID}
ENV BUILD_DATE=${BUILD_DATE}

USER root

WORKDIR /usr/src/app

ENV HOME=/usr/src/app

# Copy files from previous build
COPY --from=build --chmod=777 /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build --chmod=777 /usr/local/bin /usr/local/bin
COPY --from=build --chmod=777 /usr/src/app/main.py /usr/src/app/main.py
COPY --from=build --chmod=777 /usr/src/app/fastapi_server /usr/src/app/fastapi_server

# Permissions to allow container to run on openshift
RUN chgrp -R 0 /usr/src/app \
&& chmod -R g=u /usr/src/app

CMD python main.py