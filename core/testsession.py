__author__ = 'Serge'
from selenium import webdriver

class TestSession(object):

    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = TestSession()
        return cls.instance

    def __init__(self):
        self.driver = webdriver.Chrome()
