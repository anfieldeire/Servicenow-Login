import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from base_test import BaseTest



class TestLogin(BaseTest):
    def test_authentication(self):

        driver.get('https://url.service-now.com/')

        time.sleep(10)

        driver.switch_to.frame("gsft_main")
        driver.implicitly_wait(5)

        time.sleep(2)
        username = driver.find_element_by_id("user_name").send_keys("username")

        time.sleep(2)
        password = driver.find_element_by_id("user_password").send_keys("password")
        time.sleep(2)

        login_btn = driver.find_element_by_id('sysverb_login')
        login_btn.click()

        time.sleep(20)
        driver.switch_to.default_content()

        # Search for the user header to verify successful login
        user_header = driver.find_element(By.XPATH,
                                          '/html/body/div[5]/div/div/header/div[1]/div/div[2]/div/div[2]/div/button/div/span[1]')
        assert 'FirstName LastName' == user_header.text
