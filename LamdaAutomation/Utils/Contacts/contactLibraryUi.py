from LamdaAutomation.Library import uiLibrary
from LamdaAutomation.Library import adbLibrary

obj = uiLibrary.uiLibrary()
obj1 = adbLibrary.adbLibrary()

class contactLibraryUi():
    def __init__(self):
        pass

    def launchContactUi(self):
        obj.launchApp1("Contacts")

    def addcontact(self):
        obj.clickbyadd("com.android.dialer:id/menu_add")

    def inputfirstname(self):
        obj.inputfirstname("android.widget.EditText")
        obj1.inputname()


