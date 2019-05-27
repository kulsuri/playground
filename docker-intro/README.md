# docker-intro
python web app for introductory docker project

# Pre-requisites
- docker

# Installation Instructions
1. clone repo
```
git clone https://github.com/kulsuri/playground/docker-intro
```
2. build docker image
```
docker build -t sample-python-web-app .
```
3. run docker image
```
docker run -p 8080:8080 sample-python-web-app
```

# Running the App
- in the web browser, open:
```
localhost:8080
```