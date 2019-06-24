import os
import unittest
from repo.views import app
 
class BasicTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
 
    def tearDown(self):
        pass
 
    def test_css_loaded(self):
        response = self.app.get('/static/body.css', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_not_exisiting_page(self):
        response = self.app.get('/logins')
        self.assertEqual(response.status_code, 404)
#to do add real examples from blueprint
 
if __name__ == "__main__":
    unittest.main()