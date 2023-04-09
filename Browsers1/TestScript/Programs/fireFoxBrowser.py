# import subprocess
# import time
# from selenium.webdriver.common.by import By
#
# from Tools.scripts.win_add2path import PATH
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# # subprocess.Popen(r"C:\Users\DELL\PycharmProjects\Browsers\Drivers\geckodriver-v0.32.2-win-aarch64\geckodriver.exe",shell=True)
# #
# #
# # options = Options()
# # options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
# # driver = webdriver.Chrome(executable_path=PATH, options=options)
# #
# # def setUp(self):
# #     self.browser = webdriver.Firefox()
# #     self.addCleanup(self.browser.quit)
# # #Naviagte to Selenium
# # driver.get("https://www.selenium.dev/")
# #
# # #Mazimize current window
# # driver.maximize_window()
# #
# # #Delay execution for 10 seconds
# # time.sleep(2)
# #
# # # Close the browser
# # # driver.quit()
# # setUp()
#
# # driver = webdriver.Firefox(executable_path="C:\geckodriver.exe")
# # driver = webdriver.Edge(executable_path="msedgedriver.exe")
# driver = webdriver.Edge(r"C:\Users\DELL\PycharmProjects\Browsers\Drivers\edgedriver_win64\msedgedriver.exe")
# # driver = webdriver.Chrome(executable_path="chromedriver.exe")
# time.sleep(3)
# # to maximize the browser window
# driver.maximize_window()
# time.sleep(3)
# #get method to launch the URL
# driver.get("https://www.tutorialspoint.com/index.htm")
# time.sleep(5)
#
#
# driver = webdriver.Chrome(executable_path="chromedriver.exe")
# driver.get("https://www.w3schools.com/")
# time.sleep(3)
# #to refresh the browser
#
# driver.refresh()
# time.sleep(3)
# #to close the browser
# driver.close()
#
#


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Launch Chrome browser
driver = webdriver.Chrome()

# Open first tab and navigate to a URL
driver.get("https://www.google.com")

# Open second tab
driver.find_element('body').send_keys(Keys.CONTROL + 't')

# Switch to the second tab
driver.switch_to.window(driver.window_handles[1])

# Navigate to a different URL in the second tab
driver.get("https://www.selenium.dev")

# Close the second tab
driver.close()

# Switch back to the first tab
driver.switch_to.window(driver.window_handles[0])

# Navigate to a different URL in the first tab
driver.get("https://www.python.org")

# Close the first tab and quit the browser
driver.close()
driver.quit()