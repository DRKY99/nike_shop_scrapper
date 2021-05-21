from selenium import webdriver
import time
count =9996
NAME = "Nike"
LASTNAME = "Scrapper"
PHONE = "0000000000"
EMAIL = "NikeScrapper"+f"{count:04d}"
PASS = "NikeS"+f"{count:04d}"+"$.."
DATE = "01/01/1980"

#PROXY = "187.190.255.245:999" 
#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--proxy-server=%s' % PROXY)
#chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--ignore-ssl-errors')
#chrome_options.add_argument("--incognito")

driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://mail.tutanota.com/signup")
time.sleep(5)


elem = driver.find_element_by_xpath('//*[@id="upgrade-account-dialog"]/div[2]/div[1]/div[1]/div[4]/button/div')
elem.click()
time.sleep(1)

elem = driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[1]/div/input')
elem.click()
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[2]/div[2]/div/input')
elem.click()
time.sleep(2.1)
elem = driver.find_element_by_xpath('//*[@id="modal"]/div[2]/div/div/div/div[3]/button[2]')
elem.click()
time.sleep(6.3)


elem = driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[1]/div/div/div/div[1]/input')
elem.send_keys(EMAIL)
time.sleep(1)
elem = driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[2]/div[1]/div[1]/div/div/div[1]/input[4]')
elem.send_keys(PASS)
time.sleep(3)
elem = driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[2]/div[3]/div[1]/div/div/div/input')
elem.send_keys(PASS)
time.sleep(5)
elem = driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[3]/div/input')
elem.click()
time.sleep(1.4)
elem = driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[4]/div/input')
elem.click()
time.sleep(3.5)
elem = driver.find_element_by_xpath('//*[@id="signup-account-dialog"]/div/div[5]/button')
elem.click()
time.sleep(28.6)

