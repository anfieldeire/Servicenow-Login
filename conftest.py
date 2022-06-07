import pytest
import time
from selenium import webdriver

@pytest.fixture(scope='class')
def webdriver(request):
    from selenium import webdriver
    driver = webdriver.Firefox()
    driver.maximize_window()
    request.cls.driver = driver

    yield driver
    driver.close()

