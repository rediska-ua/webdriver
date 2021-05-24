from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox(executable_path=r'C:\\Users\\maxsh\\Downloads\\folder-geckodriver\\geckodriver.exe')
browser.get('https://www.amazon.com/')
browser.implicitly_wait(5)

expected_result = 'PlayStation 5 DualSense Wireless Controller'

browser.find_element_by_css_selector('#twotabsearchtextbox').send_keys('Playstation 5')
browser.find_element_by_css_selector('#twotabsearchtextbox').send_keys(Keys.ENTER)
data_item = browser.find_element_by_css_selector('[data-index="1"]')
data_item.find_element_by_css_selector('.a-size-medium').click()
browser.implicitly_wait(5)

actual_result = browser.find_element_by_css_selector('#productTitle').text

assert expected_result == actual_result