import unittest
from flaskapp import app
from redis import redis

class CounterTest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_welcome_page(self):
        reponse = self.app.get('/')
        self.assertEqual(reponse.status_code,200)
    def test_redis_connection(self):
        redis=Redis(host"redis_server",db=0)
        self.app.get('/visit')
        self.assertEqual(int(redis.get("counter")),1)
    if __name__ == "__main__":
        unittest.main()