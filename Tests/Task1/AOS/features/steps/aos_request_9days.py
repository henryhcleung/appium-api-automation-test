from behave import *
import os
import logging
import unittest
from time import sleep
from random import randint
from appium import webdriver

#logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    handlers=[logging.FileHandler('response.log', 'w', 'utf-8'), ])

@given('Open Hong Kong Observatory App')
def step_open_app_aos(context):
    pass

@given('User click the menu bar')
def step_click_menu_bar_aos(context):
    context.driver.find_element_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]').click()
    # pass

@when('User click the 9 days forecasts button')
def step_click_9_days_weather_button_aos(context):
    context.driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[11]/android.view.ViewGroup/android.widget.TextView').click()
    # pass

@then('User will see the next 9 days forecasts information')
def step_validate_9_days_weather_information_aos(context):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_after__next_9_days_forecasts.png")
    