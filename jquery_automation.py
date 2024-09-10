"""
Python Automation Code for Calendar widget
"""

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException


class SumanJqueryCalendarAutomation:

    url = "https://jqueryui.com/datepicker/#date-range"
    date_from = "07/20/2024"
    date_to = "08/25/2024"
    calendar_frame = "//*[@id='content']//iframe[@class='demo-frame']"
    from_month = "//div//select[@class='ui-datepicker-month']"
    to_month = "//div[@class='ui-datepicker-title']//select"
    from_day = "//div[@class='ui-datepicker-group ui-datepicker-group-first']//table//tbody//tr//td//a[@data-date='20']"
    to_day = "//div[@class='ui-datepicker-group ui-datepicker-group-first']//table//tbody//tr//td//a[@data-date='25']"
    driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(10)
        return True

    # automation code to automate jquery calendar
    def calendar(self):
        try:
            # change the frame to calendar
            frame = self.driver.find_element(by=By.XPATH, value=self.calendar_frame)
            self.driver.switch_to.frame(frame)

            # steps for FROM Date & Month
            self.driver.find_element(by=By.ID, value="from").click()
            from_month = self.driver.find_element(by=By.XPATH, value=self.from_month)
            select_from_month = Select(from_month)
            select_from_month.select_by_visible_text("Jul")
            self.driver.find_element(by=By.XPATH, value=self.from_day).click()

            # steps for TO Date & Month
            self.driver.find_element(by=By.ID, value="to").click()
            to_month = self.driver.find_element(by=By.XPATH, value=self.to_month)
            select_to_month = Select(to_month)
            select_to_month.select_by_visible_text("Aug")
            self.driver.find_element(by=By.XPATH, value=self.to_day).click()

            # fetch data from the Input-Box
            start_date = self.driver.find_element(by=By.XPATH, value="//input[@id='from']").get_attribute('value')
            end_date = self.driver.find_element(by=By.XPATH, value="//input[@id='to']").get_attribute('value')

            return [start_date, end_date]

        except (NoSuchFrameException, NoSuchElementException) as error:
            print(error)

        finally:
            self.driver.quit()

