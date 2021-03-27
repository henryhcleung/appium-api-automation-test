import os
from time import sleep
from appium import webdriver

def before_all(context):
    # context.config.setup_logging()
    pass

def before_feature(context, feature):
    app = os.path.abspath(app)
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        #Configure conrrect 'app' : '/Users/henryhcleung/MyObservatory/Tests/Task1/MyObservatory.app'
         desired_capabilities={
            'platformName' : 'iOS',
            'platformVersion' : '14.4',
            'deviceName' : 'iPhone 8 Plus'
        }
        # ,
        #     'DeviceName': "AOS_MyObervatory",
        #     'app': "/Users/henryhcleung/MyObservatory/Tests/Task1/MyObservatory.apk",
        #     'appPackage': "io.appium.android.apis",
        #     'appActivity': ".view.TextFields",
        #     'automationName': "UiAutomator2"
    )       
       
def after_feature(context, feature):
    sleep(1)
    context.driver.save_screenshot("features/reports/screen_final_IOS.png")
    context.driver.quit()