from Library.browserLibrary import browserLibrary
import time
obj = browserLibrary()

class browserLaunch():

    def launchEdge(self):
        obj.lacunchEdge()

    def openUrl(self):
        obj.openURL("https://www.facebook.com/")

    def maxWindow(self):
        obj.maxWindow()

    def class_Name_Val1(self):
        obj.textVal_By_name1(clname="_8eso",expRes="Facebook helps you connect and share with the people in your life.")

    def exitAllWindows(self):
        obj.closeAllBrowser()



