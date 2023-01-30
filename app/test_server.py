import unittest
from prometheus_client import REGISTRY
from server import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()


    def test_code_for_200(self):
        response = self.client.get("/codes")
        assert response.status_code == 200
        response_data='{"code":200}\n'
        self.assertEqual(response_data,response.get_data(as_text=True))

    def test_code_for_201(self):
        response = self.client.get("/codes/update")
        assert response.status_code == 201
        response_data='{"code":201}\n'
        self.assertEqual(response_data,response.get_data(as_text=True))
 
    def test_code_for_503(self):
        response = self.client.get("/codes/callbackend")
        assert response.status_code == 503
        response_data='{"code":503}\n'
        self.assertEqual(response_data,response.get_data(as_text=True))

  
    def test_invalid_route(self):
        response = self.client.get("/codes/wrongUrl")
        assert response.status_code == 404
        response_data='{"code":404}\n'
        self.assertEqual(response_data,response.get_data(as_text=True))

    def test_metrics_count(self):
        response = self.client.get("/metrics")
        assert response.status_code == 200
        self.assertIn("TYPE response_count_total counter",response.get_data(as_text=True))
        
  

if __name__ == "__main__":
    unittest.main()
