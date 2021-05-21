from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default&dsh=S-1106472605%3A1621566498297934&gmb=exp&biz=false&flowName=GlifWebSignIn&flowEntry=SignUp")
time.sleep(1)

elem = driver.find_element_by_xpath('//*[@id="firstName"]')
elem.send_keys("Nike")
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="lastName"]')
elem.send_keys("Scrapper")
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="username"]')
elem.send_keys("NikeScrapper8888")
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
elem.send_keys(".NikeS8888$..")
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
elem.send_keys(".NikeS8888$..")
time.sleep(0.5)
elem = driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/div/button')
elem.click()
time.sleep(0.5)



