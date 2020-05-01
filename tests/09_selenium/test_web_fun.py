from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def test_searching():
    # Given I open google
    # When I search "Golife"
    # Then I should see search result contain "GoLife: Aplikasi Penyedia Jasa Layanan Gaya Hidup"

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('https://google.co.id')
    search_box = driver.find_element_by_name('q')
    search_box.send_keys('Golife'+ Keys.ENTER)
    time.sleep(5)
    results_title = driver.find_elements_by_css_selector('h3')
    results = [title.text for title in results_title]
    print(results)
    expected_link = "GoLife: Aplikasi Penyedia Jasa Layanan Gaya Hidup"
    matches = [text for text in results if expected_link.lower() in text.lower()]
    print(matches)
    assert len(matches) > 0
    driver.quit()
    