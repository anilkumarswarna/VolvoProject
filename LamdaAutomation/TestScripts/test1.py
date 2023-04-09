from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(r"C:\Users\Srikanth\PycharmProjects\SeleniumPython\Drivers\msedgedriver.exe")

driver.get("https://www.facebook.com/")

expRes = "Facebook helps you connect and share with the people in your life."
driver.maximize_window()

fbText1 = driver.find_element(By.CLASS_NAME,"_8eso").is_displayed()

print(fbText1)

actRes = driver.find_element(By.CLASS_NAME,"_8eso").text

if(actRes == expRes):
    print("PASS")

else:
    print("FAIL")

time.sleep(4)

