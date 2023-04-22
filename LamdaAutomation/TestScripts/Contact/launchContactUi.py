from LamdaAutomation.Utils.Contacts import contactLibraryUi
import time

obj = contactLibraryUi.contactLibraryUi()

obj.launchContactUi()
time.sleep(2)
obj.addcontact()
obj.inputfirstname()