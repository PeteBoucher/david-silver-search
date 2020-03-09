#  This work is licensed under the Creative Commons Attribution-ShareAlike 2.0 Generic License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/2.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage


class SearchByPartNumberPage(BasePage):
    search_input = (By.ID, 'partnumsearchbox')
    search_results = (By.CSS_SELECTOR, 'div.productlistdesc')

    def enter_search_term(self, term):
        search_element = self.driver.find_element(*SearchByPartNumberPage.search_input)
        search_element.send_keys(term)

    def click_submit(self):
        search_element = self.driver.find_element(*SearchByPartNumberPage.search_input)
        search_element.submit()

    def search(self, term):
        self.enter_search_term(term)
        self.click_submit()

    def get_results(self):
        description = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(self.search_results))
        return description.text
