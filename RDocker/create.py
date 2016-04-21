import falcon
import json
import os
from docker import Client

#Resourse class for getContainers API
class containersClass(object):
    
    def on_get(self, req, resp):
        """Handles GET requests"""
        r = getContainer()
        resp.status = falcon.HTTP_200
      
     
        json_string = json.dumps(r)
        resp.body = json_string
        
        return
#Resource class for containerCreate Class
class containerCreateClass(object):
    
    
    def on_get(self,req,resp):
        
        print(req.params)
        r = createContainer(req.params)
        resp.status = falcon.HTTP_200
        json_string = json.dumps(r)
        resp.body = json_string
       # resp.body = "done"
        return
   
#function that calls the docker containers API on unix socket   
def getContainer():# add param cmd to send the command 
  # c = docker.Client(base_url = 'localhost:2348')
    c = Client(base_url = 'unix://var/run/docker.sock')
    container = c.containers()  
    return container

#function that calls the create_containers API on unix socket
def createContainer(params):
    
    c = Client(base_url = 'unix://var/run/docker.sock')
    ret = c.create_container(**params)
    return ret