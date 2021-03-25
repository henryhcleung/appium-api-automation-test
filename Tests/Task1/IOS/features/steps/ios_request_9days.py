from behave import *
import os
import logging
import unittest
from time import sleep
from random import randint
from appium import webdriver
from selenium.webdriver.common.keys import Keys

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

@given('Open Hong Kong Observatory App')
def step_open_app_ios(context):
    pass

@given('User click the menu bar')
def step_click_menu_bar_ios(context):
    pass

@when('User click the 9 days forecasts button')
def step_click_9_days_weather_button_iso(context):
    pass

@then('User will see the next 9 days forecasts information')
def step_validate_9_days_weather_information_iso(context):
     pass

