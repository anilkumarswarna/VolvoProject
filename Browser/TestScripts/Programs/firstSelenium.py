# import libraries or modules
import selenium.webdriver as webdriver
import time

# create instance for webdriver
driver = webdriver.Chrome(r"C:\Users\DELL\PycharmProjects\Browser\Drivers\chromedriver.exe")

#Naviagte to Selenium
driver.get("https://www.selenium.dev/")

#Mazimize current window
driver.maximize_window()

#Delay execution for 10 seconds
time.sleep(2)

# Close the browser
driver.quit()