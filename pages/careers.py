from selenium.webdriver.support.select import Select
from assertpy import assert_that
from selenium.webdriver.support.wait import WebDriverWait

from pages.base import BasePage


__author__ = 'Serge'

class CareerPage(BasePage):

    whatBy = '#gnewtonKeyword'
    departmentBy = '#gnewtonDepartment'
    whereBy = '#gnewtonLocation'
    searchBy = '#gnewtonSearchBtn'
    frameBy = '#gnewtonIframe'

    resultsRowsBy = '.gnewtonCareerGroupRowClass'

    def switch_to_frame(self):
        self.driver.switch_to_frame(self.driver.find_element('css', self.frameBy))


    def search(self, what, department, where):
        try:
            self.switch_to_frame()
            self.driver.find_element('css', self.whatBy).send_keys(what)
            Select(self.driver.find_element('css', self.departmentBy)).select_by_visible_text(department)
            self.driver.find_element('css', self.whereBy).send_keys(where)
            self.driver.find_element('css', self.searchBy).click()
        finally:
            self.driver.switch_to_default_content()

    def validate_has_results(self, num):
        try:
            self.switch_to_frame()
            # non-smart workaround
            WebDriverWait(self.driver, 5).until(lambda dr: len(dr.find_elements('css', self.resultsRowsBy)) > num)
            assert_that(len(self.driver.find_elements('css', self.resultsRowsBy))).is_greater_than_or_equal_to(num)
        finally:
            self.driver.switch_to_default_content()


