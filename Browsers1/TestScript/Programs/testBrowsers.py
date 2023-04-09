from selenium import webdriver
import time

driver = webdriver.Edge(r"C:\Users\DELL\PycharmProjects\Browsers\Drivers\edgedriver_win64\msedgedriver.exe")
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
time.sleep(3)
# to maximize the browser window
driver.maximize_window()
time.sleep(3)
#get method to launch the URL
driver.get("https://www.tutorialspoint.com/index.htm")
time.sleep(5)


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://www.w3schools.com/")
time.sleep(3)
#to refresh the browser

driver.refresh()
time.sleep(3)
#to close the browser
driver.close()