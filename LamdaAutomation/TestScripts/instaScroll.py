import time

from LamdaAutomation.Utils import instaLanguageLibrary

aj2 = instaLanguageLibrary.instaLanguageLibrary()


aj2.screenOnUi()
time.sleep(3)
aj2.screenSwipeADB()
time.sleep(3)
aj2.launchApp()
time.sleep(4)
aj2.screenScrollUi()
time.sleep(9)
aj2.back()