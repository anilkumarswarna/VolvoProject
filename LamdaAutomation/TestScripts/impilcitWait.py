'''
synchronization problems

Condition to wait for a specific period of time
to perform action on WebElement before throwing an error
NoSuchElementException.

There are two types of waits in selenium.

time
Implicitly wait
Explicit wait or WebDriverWait

'''

from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Edge(r"C:\Users\Srikanth\PycharmProjects\SeleniumPython\Drivers\msedgedriver.exe")

# set implicit wait time
driver.implicitly_wait(10) # seconds

url = "https://www.facebook.com/"

driver.get(url)

driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='email']").send_keys("kanth122121")
driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("kanth")
# driver.find_element(By.XPATH,"//button[@name='login']").click()
time.sleep(2)

driver.quit()