
# Set Base image
FROM python:3.7-alpine

# Set Maintainer
MAINTAINER victor Nwokeocha

# Python unbuffered env variable
ENV PYTHONUNBUFFERED=1

# Copy and install the requirements
COPY ./requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

# Make and cd into a dir to store app source code
RUN mkdir /app
WORKDIR /app

# copys the application to the new dir created on docker
COPY ./app /app

# Create a user to run the app on docker
# Necessary for security reasons
RUN adduser -D runner-user
USER runner-user
