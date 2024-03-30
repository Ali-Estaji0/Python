from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('https://login.yahoo.com/account/create')

input('\n\nRUN??\n\n')

FirstName = driver.find_element(By.ID, 'usernamereg-firstName')
FirstName.send_keys('Ali')

Email = driver.find_element(By.ID, 'usernamereg-userId')
Email.send_keys('aliestaji0912@yahoo.com')

Password = driver.find_element(By.ID, 'usernamereg-password')
Password.send_keys('Aliestaji0912')

Month = driver.find_element(By.ID, 'usernamereg-month')
Month.send_keys('July')

Day = driver.find_element(By.ID, 'usernamereg-day')
Day.send_keys('5')

Year = driver.find_element(By.ID, 'usernamereg-year')
Year.send_keys('2005')

sleep(2)

Btn = driver.find_element(By.XPATH, '//*[@id="reg-submit-button"]')
Btn.click()

input('\n\nEXIT??\n\n')

driver.quit()