from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

count =199
NAME = "Nike"
LASTNAME = "Scrapper"
PHONE = "5500440044"
EMAIL = ""
PASS = "NikeS"+f"{count:04d}"+"$.."
DATE = "10/05/1990"

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')

driver.get("https://www.guerrillamail.com/")
elem = driver.find_element_by_xpath('//*[@id="inbox-id"]')
EMAIL = elem.get_attribute("innerHTML")+'@';
elem = driver.find_element_by_xpath('//*[@id="gm-host-select"]')
EMAIL += str(elem.get_attribute("value"));
print(EMAIL)
time.sleep(1)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])

driver.get("http://www.innvictus.com/register")
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="register.firstName"]')
elem.send_keys(NAME)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="register.lastName"]')
elem.send_keys(LASTNAME)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="register.mobileNumber"]')
elem.send_keys(PHONE)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="register.email"]')
elem.send_keys(EMAIL)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="password"]')
elem.send_keys(PASS)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="register.checkPwd"]')
elem.send_keys(PASS)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="register.dateOfBirth"]')
elem.send_keys(DATE)
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="gender.MALE"]')
elem.click()
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="flip-button-create"]')
elem.click()
time.sleep(2)
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[2])
driver.get("http://www.innvictus.com/")