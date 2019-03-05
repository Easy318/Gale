import unittest
from gale.test.test_data import personal_data
from gale import settings
from gale.gale import Gale


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_all(self):

        self.get_cookies()
        # self.screenshot()

    def get_cookies(self):
        '''获取cookies测试
        '''

        driver = Gale()
        url = personal_data.TEST_URL
        cookies_path = settings.TEST_COOKIES_PATH
        user_data = personal_data.TEST_DATA
        driver.get_cookies(url, cookies_path, user_data)

    def screenshot(self):
        '''截图测试
        '''

        driver = Gale()
        url = personal_data.TEST_URL
        cookies_path = settings.TEST_COOKIES_PATH
        driver.get_url_by_cookies(url, cookies_path)
        driver.save2png()


if __name__ == "__main__":

    unittest.main()
