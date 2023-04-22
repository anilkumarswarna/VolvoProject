import time

from LamdaAutomation.Utils import instaloginLibrary

aj2 = instaloginLibrary.instaloginLibrary()

aj2.screenOnUi()
time.sleep(2)
aj2.screenSwipeADB()
time.sleep(2)
aj2.launchApp()
time.sleep(5)
aj2.pressBack()
time.sleep(2)

