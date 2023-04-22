from Demo.Demo.library import adbLib
import uiautomator2 as u2

d = u2.connect("KJRKLNDAYLEYVO8T")

class ui(adbLib):

    def __init__(self,id):
        super().__init__()
        global d
        d = u2.connect(id)

    def home(self):
        try:
            d.press("home")

        except Exception as e:
            raise e

    def back(self):
        try:
            d.press("back")

        except Exception as e:
            raise e

    def lock(self):
        try:
            d.screen_off()

        except Exception as e:
            raise e

    def unlock(self):
        try:
            d.screen_on()

        except Exception as e:
            raise e

    def launchApp(self,apk):
        try:
            d.app_start(apk)

        except Exception as e:
            raise e

    def closeApp(self,apk):
        try:
            d.app_stop(apk)

        except Exception as e:
            raise e

    def openBrowser(self,url):
        try:
            d.open_url(url)

        except Exception as e:
            raise e

    def touch(self,x):
        try:
            d(text=x).click()

        except Exception as e:
            raise e



