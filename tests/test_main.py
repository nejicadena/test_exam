import unittest
from flask import Flask
from flask_restful import Api
from resources.routes import initialize_routes
import json

class MainTest(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        initialize_routes(self.api)
        self.client = self.app.test_client()

    # def test_get_request(self):
    #     response = self.client.get('/example')
    #     self.assertEqual(response.status_code, 200)
    #     # Agrega aquí más aserciones para verificar la respuesta recibida

    def test_post_request(self):
        response = self.client.post('/example', json={'idUser': 2})
        self.assertEqual(response.status_code, 200)
        print(json.loads(response.data))
        self.assertEqual(json.loads(response.data)['Consulta'], "Ok")
        # Agrega aquí más aserciones para verificar la respuesta recibida

if __name__ == '__main__':
    unittest.main()