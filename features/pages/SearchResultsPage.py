#  This work is licensed under the Creative Commons Attribution-ShareAlike 2.0 Generic License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/2.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
import logging

from selenium.webdriver.common.by import By

from features.pages.BasePage import BasePage


class SearchResultsPage(BasePage):
    product_rows = (By.CLASS_NAME, 'productrow')
    logger = logging.getLogger()

    def products_count(self):
        product_row_elems = self.driver.find_elements(*SearchResultsPage.product_rows)
        return len(product_row_elems)

    def product_count_containing(self, needle):
        product_row_elems = self.driver.find_elements(*SearchResultsPage.product_rows)
        results = []
        for item in product_row_elems:
            part_description = item.text
            # self.logging.info(f'part: {part_description}')

            if needle in part_description:
                results.append(part_description)

        return len(results)
