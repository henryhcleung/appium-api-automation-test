import os
from time import sleep
from appium import webdriver

def before_all(context):
    # context.config.setup_logging()
    pass

def before_feature(context, feature):
    app = os.path.join(os.path.dirname(__file__),
                           '/Users/henryhcleung/MyObservatory/Tests/Task1/MyObservatory.apk')
    app = os.path.abspath(app)
    context.driver = webdriver.Remote(
        command_executor='http://127.0.0.1:4723/wd/hub',
        desired_capabilities={
            'platformName' : 'Android',
            'platformVersion' : '11'
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
    context.driver.save_screenshot("features/reports/screen_final_AOS.png")
    context.driver.quit()