import time

from Demo.Demo.library import adbLib
from Demo.Demo.resources.testdata import my_data


obj = adbLib.adbKeywords()

class settings(adbLib.adbKeywords):

    def __int__(self):
        pass

    def LaunchSettings(self):
        try:
            # lauch app with using testdata
            package_name = my_data["setting_package"]
            obj.launchapp(package_name)

        except Exception as e:
            raise e

    def OnWifi(self):
        try:
            obj.wifiOn()

        except Exception as e:
            raise e

    def OffWifi(self):
        try:
            obj.wifiOff()

        except Exception as e:
            raise e

    def valWifi(self):
        try:
            obj.wifiValidation()
        except Exception as e:
            raise e

    def OnBt(self):
        try:
            print("calling OnBT Function")
            obj.btOn()
            time.sleep(7)

        except Exception as e:
            raise e

    def OffBt(self):
        try:
            obj.btOff()
            time.sleep(7)
        except Exception as e:
            raise e

    def valBt(self):
        try:
            obj.btValidation()
        except Exception as e:
            raise e

    def Onlocation(self):
        try:
            obj.locationOn()

        except Exception as e:
            raise e

    def Offlocation(self):
        try:
            obj.locationOff()

        except Exception as e:
            raise e

    def valLocation(self):
        try:
            obj.locationValidation()
        except Exception as e:
            raise e

    def OnAireplaneMode(self):
        try:
            obj.aireplaneOn()

        except Exception as e:
            raise e

    def OffAireplaneMode(self):
        try:
            obj.aireplaneOff()

        except Exception as e:
            raise e

    def valAirplaneMode(self):
        try:
            obj.aireplaneModeValidation()
        except Exception as e:
            raise e

    def OnData(self):
        try:
            obj.dataOn()

        except Exception as e:
            raise e

    def OffData(self):
        try:
            obj.dataOff()

        except Exception as e:
            raise e

    def valData(self):
        try:
            obj.dataValidation()
        except Exception as e:
            raise e
