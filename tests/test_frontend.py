import unittest
from app import app

class TestFrontendApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_list_todos_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_create_todo_route(self):
        response = self.app.get('/create')
        self.assertEqual(response.status_code, 200)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()
