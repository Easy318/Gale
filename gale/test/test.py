import unittest
from gale.test_data import settings
from gale.gale import Gale


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_cookies(self):
        '''获取cookies测试
        '''

        driver = Gale()
        url = settings.TEST_URL
        user_data = settings.TEST_DATA
        cookies_path = settings.TEST_COOKIES_PATH
        driver.get_cookies(url, cookies_path, user_data)


if __name__ == "__main__":

    unittest.main()
