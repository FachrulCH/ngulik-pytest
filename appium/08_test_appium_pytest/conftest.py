import pytest
from appium import webdriver

APP_IOS = "https://github.com/cloudgrey-io/the-app/releases/download/v1.10.0/TheApp-v1.10.0.ipa"

@pytest.fixture(scope='function')
def driver():
    # caps = {
    #     'platformName': 'Android',
    #     'deviceName': 'Android',
    #     'appPackage': 'com.google.android.apps.meetings',
    #     'appActivity': '.splash.SplashActivity',
    #     'noReset': True,
    #     'automationName': 'UiAutomator2'
    # }
    caps = {
        'platformName': 'iOS',
        'deviceName': 'iPhone 5s',
        'platformVersion': '12.4',
        'udid': 'auto',
        'xcodeSigningId': 'iPhone Developer',
        'app': APP_IOS
    }
    _driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
    _driver.implicitly_wait(10)
    yield _driver
    _driver.quit()
