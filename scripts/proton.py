from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


import time

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://mail.protonmail.com/create/new?language=en")
time.sleep(3)
elem = driver.find_element_by_xpath('//*[@id="password"]')
elem.clear()
elem.send_keys("NikeScrapper8888.")
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="passwordc"]')
elem.clear()
elem.send_keys("NikeScrapper8888.")
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="mainContainer"]/div/div/div[1]/form/div[1]/div[1]/div/div/div[2]/iframe')
elem.click()
actions = ActionChains(driver)
actions.send_keys('NikeScrapper8888')
actions.perform()
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="mainContainer"]/div/div/div[1]/form')
elem.submit()
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="confirmModalBtn"]')
elem.click()
time.sleep(3)
elem = driver.find_element_by_xpath('//*[@id="verification-panel"]/div[6]/iframe')
elem.click()
time.sleep(1)
elem = driver.find_element_by_xpath('/html/body/div[2]/div[4]/iframe')
elem.click()