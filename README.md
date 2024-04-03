# Dockerizing

For repeating experiments with dockerizing you need to have installed git and docker

For each expirement you can just repeat this actions:
```bash
$ git clone <repo-url> .
```
```bash
$ docker build -t <image-name> .
```
```bash
$ docker run -p <port>:<port> <image-name>
```