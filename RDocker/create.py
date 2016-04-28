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
    
#Resource class for starting the created container
class containerStartClass(object):
    
    
    def on_get(self,req,resp):
        
        print(req.params)
        r = startContainer(req.params)
        resp.status = falcon.HTTP_200
        
        resp.body = "".join(r)
       # resp.body
        return

#Resource class to get the application logs from the deployed container
class containerGetlogs(object):
    
    
    def on_get(self,req,resp):
        
        print(req.params)
        r = getlogs(req.params)
        resp.status = falcon.HTTP_200
        resp.stream  = r
        resp.stream_len = r
        yield
   
#function that calls the docker containers API on unix socket   
def getContainer():# add param cmd to send the command 
  # c = docker.Client(base_url = 'localhost:2348')
    c = Client(base_url = 'unix://var/run/docker.sock')
    container = c.containers()  
    return container

#function that calls the create_containers API on unix socket
def createContainer(params):
    
    if 'detach' in params:
        params['detach'] = bool(params['detach'] )
      
    if 'stdin_open' in params:
        params['stdin_open'] = bool( params['stdin_open'])
    
    if 'tty' in params:
        params['tty'] = bool( params['tty'])
   
    if 'network_disabled' in params:
        params['network_disabled'] = bool( params['network_disabled'])
    
    c = Client(base_url = 'unix://var/run/docker.sock')
    ret = c.create_container(**params)
    return ret
    
    
def startContainer(params):# add param cmd to send the command 
    c = Client(base_url = 'unix://var/run/docker.sock')
    cid = {}
    cid["container"] = params['container']
    print(cid)
    
    if 'logs' in params:
        
        if bool(params['logs']) is True:
            
            try:
                del params['logs']
            except KeyError:
                pass
            
            if 'stdout' in params:
                params['stdout'] = bool(params['stdout'])
            
            if 'stdin' in params:
                params['stdin'] = bool(params['stdin'])
                
            if 'stream' in params:
                params['stream'] = bool(params['stream'])
    
            if 'stderr' in params:
                params['stderr'] = bool(params['stderr'])
            
            if 'timestamps' in params:
                params['timestamps'] = bool(params['timestamps'])
            
            if 'tail' in params:
                if isdigit(params['tail']):
                    params['tail'] = int(params['tail'])
                   
            
            container = c.start(**cid)
            container = c.logs(**params)
    else:
        container = c.start(**cid)
   
    return container

def getlogs(params):
    
    c = Client(base_url = 'unix://var/run/docker.sock')
    
    if 'stdout' in params:
        params['stdout'] = bool(params['stdout'])
    
    if 'stdin' in params:
        params['stdin'] = bool(params['stdin'])
        
    if 'stream' in params:
        params['stream'] = bool(params['stream'])

    if 'stderr' in params:
        params['stderr'] = bool(params['stderr'])
    
    if 'timestamps' in params:
        params['timestamps'] = bool(params['timestamps'])
    
    if 'tail' in params:
        if isdigit(params['tail']):
            params['tail'] = int(params['tail'])
    
    container = c.logs(**params)
    
    yield  container
           