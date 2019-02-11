# Set Base image
FROM python:3.7-alpine

# Set Maintainer
LABEL maintainer="Victor Nwokeocha"

# Python unbuffered env variable
ENV PYTHONUNBUFFERED 1

# Copy and install the requirements
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install --upgrade pip \
      && pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Make and cd into a dir to store app source code
RUN mkdir /app
WORKDIR /app

# copys the application to the new dir created on docker
COPY ./ /app

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

# Create a user to run the app on docker
# Necessary for security reasons
RUN adduser -D runner-user

# Make user owner of the dir
RUN chown -R runner-user:runner-user /vol/
RUN chmod 755 /vol/web

USER runner-user
