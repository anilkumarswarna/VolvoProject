from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\Browser\Drivers\chromedriver.exe")

driver.get("https://www.google.com/")

# url = "https://www.google.com/"

# driver.get(url)

driver.get("https://www.google.com/")

driver.maximize_window()
time.sleep(5)
#Search Bar
driver.find_element(By.NAME,"q").send_keys("w3Schools")
time.sleep(3)

#Click Google searh button
driver.find_element(By.NAME,"btnK").click()
time.sleep(5)

#W3school website url click
driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div/div/div/div/div/div[1]/a/h3").click()
time.sleep(10)

#Tutorials drop down
driver.find_element(By.ID,"navbtn_tutorials").click()
time.sleep(5)

#click learning Python
driver.find_element(By.XPATH,"//*[@id='nav_tutorials']/div/div/div[3]/a[9]").click()
time.sleep(4)

# scroll down the webpage
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.END)
time.sleep(10)

# scroll up the webpage
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.HOME)
time.sleep(10)

for home in range(5):
    time.sleep(3)
    driver.back()

