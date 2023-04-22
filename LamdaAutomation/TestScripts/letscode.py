from asyncio import wait

from Utils.browserLaunch import browserLaunch
import time

obj = browserLaunch()
obj.launchChrome()
obj.maxWindow()
obj.openUrl()
obj.maxWindow()
obj.click()
obj.chechBox()
obj.dropDown()
obj.implicit_wait()
obj.windows_Handling()
obj.manage_Popups()
time.sleep(4)