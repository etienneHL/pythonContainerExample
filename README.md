Each command need to be executed from the project main directory.
A PowerShell terminal has to be used on Windows. 

= BUILD = 
docker build -q -t my-python-app .

= RUN =
docker run -it --rm -v ${PWD}/app:/container/app --name my-running-app my-python-app