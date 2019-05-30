# Base Image
FROM ubuntu:latest

# Commands to create new user
RUN useradd silly_user

# Command to define the user account the image will use
USER silly_user

# Command to run when the container starts: print the current user of the image
CMD whoami