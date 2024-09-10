"""
Pytest code to validate the working of Calendar widget
"""

from jquery_automation import SumanJqueryCalendarAutomation
import pytest

calendar = SumanJqueryCalendarAutomation()


# Pytest-1 : Start the automation
def test_start():
    assert calendar.start() == True
    print("SUCCESS : Automation Started")


# Pytest-2 : Validate the working of jQuery Calendar
def test_calendar():
    test_start_date = "07/20/2024"
    test_end_date = "08/25/2024"
    assert calendar.calendar() == [test_start_date, test_end_date]
    print("SUCCESS : Calendar date tested")
