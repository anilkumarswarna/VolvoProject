from LamdaAutomation.Library import uiLibrary
from LamdaAutomation.Library import adbLibrary

aj1 = uiLibrary.uiLibrary()
aj2 = adbLibrary.adbLibrary()


class instaloginLibrary():


    def screenOnUi(self):
        aj1.screenOnUi()

    def screenSwipeADB(self):
        aj2.screenSwipeADB()

    def launchApp(self):
        aj1.launchApp("Instagram Lite")
        print("launch app sucessfully")

    def userName(self):
        aj2.userNameInput()

    def clickPasswordUi(self):
        aj1.passwordUi()

    def passwordInputADB(self):
        aj2.passwordInput()

    def clickLoginButtonUi(self):
        aj1.loginButtonUi()

    def clickRememberButtonUi(self):
        aj1.rememberButtonUi()

    def pressBack(self):
        aj1.pressBack()






