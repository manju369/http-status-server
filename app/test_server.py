import unittest
from server import app
from prometheus_client import REGISTRY

#app = codeFor200()

#app.app_context().push()

class TestMyFunction(unittest.TestCase):
    def test_metric_incremented(self):
       #with app.app_context():
        before =  REGISTRY.get_sample_value('response_count_total')
        app.codeFor200()
        after = REGISTRY.get_sample_value('response_count_total')
        self.assertEqual(1, after - before)


if __name__ == "__main__":
    unittest.main()
