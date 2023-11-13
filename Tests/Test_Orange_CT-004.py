import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select



driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait (4)
driver.maximize_window()

#login
driver.find_element(By.XPATH,'//*[@name="username"]').send_keys('Admin')
driver.find_element(By.XPATH,'//*[@name="password"]').send_keys('admin123')
driver.find_element(By.XPATH,'//*[@type="submit"]').click()
dashgbord = driver.find_element(By.CSS_SELECTOR,'span h6 ')
assert dashgbord.is_displayed()

#click pim
driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()


# organização
driver.find_element(By.CSS_SELECTOR,'div:nth-child(2) > div > i').click()
driver.find_element(By.CSS_SELECTOR,'div:nth-child(2) > div > div > ul > li:nth-child(1)').click()
validarção = driver.find_element(By.CSS_SELECTOR,' div.oxd-table-body > div:nth-child(2) > div > div:nth-child(2)').text
assert validarção == " " or "0001"

#feito