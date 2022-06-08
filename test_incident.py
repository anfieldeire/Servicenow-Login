import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from base_test import BaseTest
from test_login import TestLogin
#from custom_logger import custom_Logger


class TestIncident(BaseTest):

    def test_create(self):

        TestLogin.test_authentication(self)

        driver = self.driver
        driver.switch_to.default_content()
        time.sleep(10)

        # Left Nav, incident.do
        createnew = driver.find_element_by_id("filter")
        createnew.send_keys("incident.do")
        time.sleep(1)
        createnew.send_keys(Keys.RETURN)
        time.sleep(10)

        # switch to main frame to create the incident
        driver.switch_to.frame("gsft_main")
        time.sleep(5)

        category = driver.find_element_by_id("incident.category")
        category.send_keys("Software")
        time.sleep(2)

        subcategory = driver.find_element_by_id("incident.subcategory").send_keys("Email")
        time.sleep(2)

        callerbox = driver.find_element_by_id("sys_display.incident.caller_id")
        callerbox.send_keys("Abraham Lincoln")
        time.sleep(1)
        callerbox.send_keys(Keys.RETURN)
        time.sleep(1)

        contacttype = driver.find_element_by_id("incident.contact_type")
        contacttype.send_keys("Email")
        time.sleep(1)

        impact = driver.find_element_by_id("incident.impact")
        impact.send_keys("2")
        time.sleep(1)

        urgency = driver.find_element_by_id("incident.urgency")
        urgency.send_keys("2")
        time.sleep(1)

        assign_grp = driver.find_element_by_id("sys_display.incident.assignment_group")
        assign_grp.send_keys("Database")
        assign_grp.send_keys(Keys.RETURN)

        time.sleep(1)

        short_desc = driver.find_element_by_id("incident.short_description")
        short_desc.send_keys(f'{self.identifier} {self.module} {self.action} {self.today}')
        time.sleep(1)

        desc = driver.find_element_by_id("incident.description")
        desc.send_keys(f'{self.identifier} {self.module} {self.action} {self.today}')
        time.sleep(1)

        incident_field = driver.find_element_by_id("incident.number")
        incident_number = incident_field.get_attribute('value')
        print("Inc number: {}".format(incident_number))
        self.incident_number = incident_number

        hamburger_menu = driver.find_element(By.XPATH,
                                             '//*[@id="section-bf1d96e3c0a801640190725e63f8ac80.header"]/nav/div/div[1]/button[2]')
        hamburger_menu.click()
        save = driver.find_element(By.XPATH, '//*[@id="context_1"]/div[2]')
        save.click()

        # Find update button - if the update button is visble this confirms the incident was saved
        update_button = driver.find_element_by_id('sysverb_update')
        print(f"update button text {update_button.text}")
        assert 'Update' == update_button.text