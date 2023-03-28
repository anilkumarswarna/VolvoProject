import time

from LamdaAutomation.Utils import instaloginLibrary
from LamdaAutomation.Utils import instaLanguageLibrary

aj2 = instaloginLibrary.instaloginLibrary()
aj3 = instaLanguageLibrary.instaLanguageLibrary()


aj2.screenOnUi()
time.sleep(2)
aj2.screenSwipeADB()
time.sleep(2)
aj2.launchApp()
time.sleep(5)
aj2.userName()
time.sleep(10)
aj2.clickPasswordUi()
time.sleep(3)
aj2.passwordInputADB()
time.sleep(5)
aj2.clickLoginButtonUi()
time.sleep(10)
aj2.clickRememberButtonUi()
time.sleep(10)
aj2.pressBack()
################################










