# users-in-docker
playing with user accounts in a ubuntu docker file

# Pre-requisites
- docker

# Installation Instructions
1. clone repo
```
git clone https://github.com/kulsuri/playground/tree/master/users-in-docker
```
2. build docker image
```
docker build -t users-in-docker .
```
3. run docker image
```
docker run users-in-docker
```

# Running the App
- nothing to run :)
- the terminal should read
```
silly_user
```
- to see which folders the user silly_user has access to, run
```
docker run users-in-docker ls -l /
```
- we see that silly_user has ownership of the /app folder whereas the root user has access to the rest
```
total 68
drwxr-xr-x   1 silly_user root 4096 May 30 19:49 app
drwxr-xr-x   2 root       root 4096 May 15 14:07 bin
drwxr-xr-x   2 root       root 4096 Apr 24  2018 boot
drwxr-xr-x   5 root       root  340 May 30 19:50 dev
drwxr-xr-x   1 root       root 4096 May 30 19:50 etc
drwxr-xr-x   2 root       root 4096 Apr 24  2018 home
drwxr-xr-x   8 root       root 4096 May 23  2017 lib
drwxr-xr-x   2 root       root 4096 May 15 14:06 lib64
drwxr-xr-x   2 root       root 4096 May 15 14:06 media
drwxr-xr-x   2 root       root 4096 May 15 14:06 mnt
drwxr-xr-x   2 root       root 4096 May 15 14:06 opt
dr-xr-xr-x 144 root       root    0 May 30 19:50 proc
drwx------   2 root       root 4096 May 15 14:07 root
drwxr-xr-x   1 root       root 4096 May 15 21:20 run
drwxr-xr-x   1 root       root 4096 May 15 21:20 sbin
drwxr-xr-x   2 root       root 4096 May 15 14:06 srv
dr-xr-xr-x  13 root       root    0 May 30 19:50 sys
drwxrwxrwt   2 root       root 4096 May 15 14:07 tmp
drwxr-xr-x   1 root       root 4096 May 15 14:06 usr
drwxr-xr-x   1 root       root 4096 May 15 14:07 var
```
- to open the whoami.txt file, run:
```
docker run users-in-docker cat whoami.txt
```
- the contents of the whoami.txt file should print to the terminal:
```
silly_user
```
