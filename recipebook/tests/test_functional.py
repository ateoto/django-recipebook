from django.test import LiveServerTestCase
from django.test.client import Client

from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        cls.browser = webdriver.Firefox()
        cls.browser.implicitly_wait(3)
        super(NewVisitorTest, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()

    def setUp(self):
        self.client = Client()
