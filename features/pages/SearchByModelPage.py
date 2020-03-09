#  This work is licensed under the Creative Commons Attribution-ShareAlike 2.0 Generic License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/2.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from features.pages.BasePage import BasePage


class SearchByModelPage(BasePage):

    URL = "https://www.davidsilverspares.co.uk/parts/by-model/"

    engine_size_input = (By.NAME, 'partmodelsearch')
    model_select = (By.ID, 'partnumsearchbox')
    search_button = (By.CLASS_NAME, 'partsearchbutton')

    def enter_engine_size(self, capacity):
        engine_size_input_elem = self.driver.find_element(*SearchByModelPage.engine_size_input)
        engine_size_input_elem.send_keys(capacity)

    def click_submit(self):
        search_button_elem = self.driver.find_element(*SearchByModelPage.search_button)
        search_button_elem.click()

    def search_by_engine_size(self, capacity):
        self.enter_engine_size(capacity)
        self.click_submit()

    def select_model(self, model):
        model_select_elem = Select(self.driver.find_element(*SearchByModelPage.model_select))
        model_select_elem.select_by_value(model)

    def search_by_model(self, model, capacity):
        self.search_by_engine_size(capacity)
        # self.select_model(model)
        # self.click_submit()

    def opem(self):
        self.driver.get(self.URL)