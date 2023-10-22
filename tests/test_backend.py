import unittest
from app import app

class TestBackendApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task_route(self):
        response = self.app.post('/add', data={'task': 'Test Task'})
        self.assertEqual(response.status_code, 302)  # Redirect to index

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
