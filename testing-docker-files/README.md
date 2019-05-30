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