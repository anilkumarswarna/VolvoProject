from asyncio import wait

from Utils.browserLaunch import browserLaunch
import time

obj = browserLaunch()
obj.launchChrome()
obj.maxWindow()
obj.openUrl()
obj.textVal_ByClsName()
obj.imgVal_ByClsName()
obj.userName_ByID()
obj.password_BYName()
# obj.password11()
# obj.Button()
obj.clear_Text()
obj.forgot_Pass()
obj.back()
time.sleep(4)
obj.userName_ByID()
obj.password_BYName()
time.sleep(5)
obj.link_BY_Click()
time.sleep(5)
obj.back()
obj.partail_Link_ByText()
time.sleep(5)
obj.back()
obj.input_start_with()
time.sleep(5)
obj.OR_And()

obj.exit_allBrowsers()









