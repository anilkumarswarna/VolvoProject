# import time
#
# from selenium import webdriver
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.google.com/")
#
# #lets open google.com in the first tab
# driver.get('http://google.com')
#
# # Lets open https://www.bing.com/ in the second tab
# driver.execute_script("window.open('about:blank','secondtab''thirdtab');")
# driver.switch_to.window("secondtab")
# for i in range(4):
#     driver.get('https://www.bing.com/')
#     driver.switch_to.window("thirdtab")
#
# # # Lets open https://www.facebook.com/ in the third tab
# # driver.execute_script("window.open('about:blank','thirdtab');")
# # driver.switch_to.window("thirdtab")
# # driver.get('https://www.facebook.com/')

# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1