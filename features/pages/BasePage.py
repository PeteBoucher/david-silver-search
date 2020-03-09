#  This work is licensed under the Creative Commons Attribution-ShareAlike 2.0 Generic License. To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/2.0/ or send a letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
import logging


class BasePage(object):

    def __init__(self, context):
        LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
        logging.basicConfig(level=logging.INFO,
                            format=LOG_FORMAT)
        self.logger = logging.getLogger()

        self.driver = context.driver
        self.driver.implicitly_wait(5)
        self.timeout = 30
