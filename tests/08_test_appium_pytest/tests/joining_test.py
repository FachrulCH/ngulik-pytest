import time

from appium import webdriver


class TestJoining():
    ROOM = 'wfn-enks-pcj'

    def test_join_meeting(self, driver: webdriver.Remote):
        driver.find_element_by_id('enter_meeting_code_button').click()
        time.sleep(3)
        driver.find_element_by_id('join_meeting_edittext').send_keys(self.ROOM)
        driver.find_element_by_id('join_meeting_positive_button').click()
        driver.find_element_by_id('greenroom_join_button').click()
        assert driver.find_element_by_id(
            'greenroom_sub_header').text == "You'll join the meeting when someone lets you in"
        time.sleep(5)
