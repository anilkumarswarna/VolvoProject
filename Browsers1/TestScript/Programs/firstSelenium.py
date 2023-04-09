# import libraries or modules
# from lib2to3.pgen2 import driver

import selenium.webdriver as webdriver
import time

# create instance for webdriver
# driver = webdriver.Chrome(r"C:\Users\DELL\PycharmProjects\Browser\Drivers\chromedriver.exe")

driver = webdriver.Edge(r"C:\Users\DELL\PycharmProjects\Browsers\Drivers\edgedriver_win64\msedgedriver.exe")

# driver = webdriver.Firefox (r"C:\Users\DELL\PycharmProjects\Browsers\Drivers\edgedriver_win64\msedgedriver.exe")

#Naviagte to Selenium
driver.get("https://www.selenium.dev/")

#Mazimize current window
driver.maximize_window()

#Delay execution for 10 seconds
time.sleep(2)

driver.get("https://www.facebook.com/")

# Close the browser
driver.quit()