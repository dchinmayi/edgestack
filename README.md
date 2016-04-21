Launching Coudlet webService: this doccument is for ubuntu

Cloudlet at edge computing node uses Falcon Rest Framework to offer RestAPI's for the user and cloud to manage dockers.

Instruction:

1) Install pyhton falcon web frameworkInstances of falcon.API are WSGI applications and can run on any WSGI server, such as Gunicorn:
	debian: pip install falcon

2) Instances of falcon.API are WSGI applications and can run on any WSGI server, such as Gunicorn.
	debian:sudo apt-get install gunicorn


3) Have docker installed and make sure your docker daemon is running
	 https://docs.docker.com/engine/installation/linux/ubuntulinux/

4) running webserver, run this as a root or sudo
	debian: sudo gunicorn -b 0.0.0.0:8000 launch:api 
	
	running the above command should launch the webserver.
	you can run the server as a daemon  
	sudo gunicorn -b 0.0.0.0:8000 launch:api&

5) once the webserver is running it can manage dockers through the RestAPIs 
