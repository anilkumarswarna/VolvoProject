# # # # n = int(input("Enter the value:"))
# # # # m = int(input("How many fibinacci numbers u want :"))
# # # # n1 = 0
# # # # n2 = 1
# # # # while n<=m:
# # # #     aj =n1 + n2
# # # #     n1 = n2
# # # #     n2 = aj
# # # #     n+=1
# # # #     print(n2)
# # #
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # import time
# # #
# # # driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\SeleniumPython\Drivers\chromedriver.exe")
# # # time.sleep(5)
# # #
# # # driver.get("https://www.instagram.com/")
# # # time.sleep(5)
# # # driver.find_element(By.ID,"username-field").send_keys("value")
# # # time.sleep(5)
# # # driver.find_element(By.NAME,"password").send_keys("Password")
# # # time.sleep(5)
# # # Button = driver.find_element(By.ID,"login-form-submit")
# # # Button.click()
# # # time.sleep(5)
# # # from selenium import webdriver
# # # import time
# # # import json
# #
# # driver = webdriver.PhantomJS(executable_path='/usr/local/lib/node_modules/phantomjs/lib/phantom/bin/phantomjs')
# #
# # driver.get("http://www.google.com")
#
#
# # alerts / popups - it's not a webelemnt
#
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# import time
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Edge(r"C:\Users\Srikanth\PycharmProjects\SeleniumPython\Drivers\msedgedriver.exe")
#
# url = "https://www.letskodeit.com/practice"
#
# driver.get(url)
#
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//input[@id='alertbtn']").click()
# time.sleep(2)
#
# alrtWin = driver.switch_to.alert
# print("alret-",alrtWin.text)
# alrtWin.accept()
#
#
# time.sleep(2)
#
# driver.find_element(By.XPATH,"//input[@id='confirmbtn']").click()
# alrtWin1 = driver.switch_to.alert
# time.sleep(2)
# alrtWin1.dismiss()
# time.sleep(2)
#
#
# url2 = "https://mypage.rediff.com/login/dologin"
# driver.get(url2)
# driver.find_element(By.XPATH,"//input[@value='Login']").click()
# time.sleep(3)
# driver.switch_to.alert.accept()
# time.sleep(2)

#try to get window Id's...not same and it will change dynamically

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

driver = webdriver.Edge(r"C:\Users\Srikanth\PycharmProjects\SeleniumPython\Drivers\msedgedriver.exe")

url = "https://www.letskodeit.com/practice"
# url = "https://www.google.com/"

driver.get(url)

driver.maximize_window()


windowId = driver.current_window_handle
print("windowId: ",windowId)

'''
driver.find_element(By.XPATH,'//*[@id="opentab"]').click()

windsIds = driver.window_handles

firsttWindow = windsIds[0]
secondWindow = windsIds[1]

driver.switch_to.window(firsttWindow)

driver.find_element(By.ID,"bmwradio").click()
'''
driver.find_element(By.ID,"openwindow").click()
time.sleep(5)
# driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]").click()
windowsIds = driver.window_handles
print("windowsIds: ", windowsIds)

for i in windowsIds:
    driver.switch_to.window(i)
    print("title",driver.title)

newWind = windowsIds[1]
driver.switch_to.window(newWind)

driver.find_element(By.XPATH,'//*[@id="navbar-inverse-collapse"]/div/div/a').click()
time.sleep(5)

firstWind = windowsIds[0]
driver.switch_to.window(firstWind)

driver.find_element(By.ID,'bmwradio').click()
time.sleep(5)
driver.quit()
