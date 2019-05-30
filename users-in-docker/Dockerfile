# Base Image
FROM ubuntu:latest

# Commands to create new user
RUN useradd silly_user

# Working directory for which user silly_user has access to
WORKDIR /app

# Command to change ownership of the /app directory to the new user: silly_user
RUN chown silly_user /app

# Command to define the user account the image will use
USER silly_user

# Command to write whoami command (silly_user) to a text file
RUN whoami > whoami.txt

# Command to run when the container starts: print the current user of the image
CMD whoami