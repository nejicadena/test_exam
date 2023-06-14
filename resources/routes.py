from resources.example_resource import CreateComent

def initialize_routes(api):
    api.add_resource(CreateComent, '/example')