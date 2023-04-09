# # import MySQLdb
# #
# # # Open database connection
# # db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
# #
# # # prepare a cursor object using cursor() method
# # cursor = db.cursor()
# #
# # # execute SQL query using execute() method.
# # cursor.execute("SELECT VERSION()")
# #
# # # Fetch a single row using fetchone() method.
# # data = cursor.fetchone()
# # print("Database version : %s " % data)
# #
# # # disconnect from server
# # db.close()
#
# #import selenium.webdriver as webdriver
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome(r"C:\Users\user\PycharmProjects\Browser\Drivers\chromedriver.exe")
#
# # url = "https://www.twitter.com/"
#
#
# driver.get("https://www.twitter.com/")
#
# driver.maximize_window()
#
# time.sleep(3)
#
# # driver.getTitle()
#
# # Getting current URL source code
# actRes = driver.title
#
# # Printing the title of this URL
# print("get title",actRes)
#
# expRes = "twitter – log in or sign up"
#
# if(actRes == expRes):
#     print("Website Title is matched :PASS")
# else:
#     print("Website Title is not matched :FAIL")
#
# # Getting current URL source code
# exp_current_url = "https://twitter.com/"
# act_current_url = driver.current_url
#
# # Printing the title of this URL
# print("current url",act_current_url)
#
# if (act_current_url == exp_current_url):
#     print("Website URL is matched :PASS")
# else:
#     print("Website URL is not matched :FAIL")
#
# driver.quit()



