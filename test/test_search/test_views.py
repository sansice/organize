import unittest
from general import utils
from search import views


class TestWordCloud(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    def test_get_config_json(self):
        views.index_post()


if __name__ == '__main__':
    unittest.main()
