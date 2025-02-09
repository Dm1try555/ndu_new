import requests
from endpoints.base_endpoint import Endpoint

class PutObject(Endpoint):

    def update_by_id(self, payload, object_id):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{object_id}',json=payload).json()
        self.response_json = self.response.json()

    def check_response_name(self, name):
        assert self.response_json['name'] == name


