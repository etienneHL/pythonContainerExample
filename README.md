### PREREQUISITES
* [Docker](https://docs.docker.com/get-docker/) need to be installed.
* Each command need to be executed from the repository main directory.
* On Windows, A PowerShell terminal has to be used.

### BUILD
```docker build -q -t my-python-app .```

### RUN 
```docker run -it --rm -v ${PWD}/app:/container/app --name my-running-app my-python-app```
