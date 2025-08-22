import unittest
from app import app

class CowsayAppTestCase(unittest.TestCase):
    def setUp(self):
        # Set up a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_get_request(self):
        # Test GET request returns status code 200
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cowsay Web App', response.data)

    def test_post_request_with_message(self):
        # Test POST request with message returns cowsay output
        response = self.app.post('/', data={'message': 'Hello, test!'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, test!', response.data)