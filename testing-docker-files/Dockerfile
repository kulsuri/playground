# Base Image
FROM ubuntu:latest

# Set environment variables which can be used in the Dockerfile + evironment of container
ENV appDir=/app message="Welcome to our app!"

# Working directory
WORKDIR $appDir

# Commands to run to install dependencies: message variable will be written to README.txt
RUN echo ${message} > README.txt

# Command to run when the container starts
CMD echo Read ${appDir}/README.txt for a friendly greeting!