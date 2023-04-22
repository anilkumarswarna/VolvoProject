from selenium import webdriver
import time
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as ec

#driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\SeleniumPython\Drivers\chromedriver.exe")
driver = webdriver.Edge(r"C:\Users\user\PycharmProjects\SeleniumPython\Drivers\msedgedriver.exe")

driver.get("http://www.dummypoint.com/seleniumtemplate.html")
time.sleep(2)

exWait = WebDriverWait(driver,25,poll_frequency=5,ignored_exceptions=[ElementNotVisibleException,NoSuchElementException])
ele = exWait.until(ec.presence_of_element_located((By.ID,"user_input")))
ele.send_keys("explicity wait")

#time.sleep(5)
driver.quit()