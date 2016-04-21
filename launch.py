import falcon
import json
from RDocker import create

api = application = falcon.API()

class_containers = create.containersClass()
class_createDocker = create.containerCreateClass()

# add RestAPI route here and map the corresponding resource class
api.add_route('/containers', class_containers )
api.add_route('/run', class_createDocker)