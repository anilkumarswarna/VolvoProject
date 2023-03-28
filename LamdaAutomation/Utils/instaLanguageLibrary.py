from LamdaAutomation.Library import uiLibrary
from LamdaAutomation.Library import adbLibrary

aj1 = uiLibrary.uiLibrary()
aj2 = adbLibrary.adbLibrary()


class instaLanguageLibrary():


    def screenOnUi(self):
        aj1.screenOnUi()

    def screenSwipeADB(self):
        aj2.screenSwipeADB()

    def launchApp(self):
        aj1.launchApp("Instagram Lite")
        print("launch app sucessfully")

    def clickProfileUi(self):
        aj1.profileUi()

    def clickByMenuUi(self):
        aj1.menuUi()

    def clickBySettingsUi(self):
        aj1.settingsUi()

    def clickLanguageUi(self):
        aj1.languageUI()

    def searchLanguageUi(self):
        aj1.lagSearchUI("Search")
        print("Language searching sucessfully")

    def langInputTeluguADB(self):
        aj2.langInputADB()

    def clickUi(self):
        aj1.clickLangUi()

    def searchEnglishLanguageUi(self):
        aj1.lagSearchUI("Search")
        print("Language searching sucessfully")

    def searchEnglishLangUi(self):
        aj1.langsearchUI3("శోధించండి")
        print("English Language searched sucessfully")

    def languageInputEnglishADB(self):
        aj2.languageEnglishADB()

    def back(self):
        aj1.pressBack()

    def screenScrollUi(self):
        aj1.scrollUI()






