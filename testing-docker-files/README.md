# testing-docker-files
playing with a ubuntu docker file

# Pre-requisites
- docker

# Installation Instructions
1. clone repo
```
git clone https://github.com/kulsuri/playground/tree/master/testing-docker-files
```
2. build docker image
```
docker build -t testing-docker-files .
```
3. run docker image
```
docker run testing-docker-files cat /app/README.txt
```

# Running the App
- nothing to run :)
- the terminal should read
```
Welcome to our app!
```

# Running the App V2: see environment variables
- run docker image with interactive shell with /bin/sh command - this will run the container and launch a shell
```
docker run -it testing-docker-files /bin/sh
```
- run the set command in the interactive shell
```
# set
```
- we should now see the settings for the environment variables of the image:
```
HOME='/root'
HOSTNAME='722575e4c902'
IFS='
'
OPTIND='1'
PATH='/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
PPID='0'
PS1='# '
PS2='> '
PS4='+ '
PWD='/app'
TERM='xterm'
appDir='/app'
message='Welcome to our app!'
```