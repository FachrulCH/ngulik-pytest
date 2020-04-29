from appium import webdriver

caps = {
    'platformName': 'Android',
    'deviceName': 'Android',
    'appPackage': 'com.google.android.apps.meetings',
    'appActivity': '.splash.SplashActivity',
    'noReset': True
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(5)
driver.find_element_by_id('enter_meeting_code_button').click()
driver.quit()
