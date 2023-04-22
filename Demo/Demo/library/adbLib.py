import subprocess
import time
from datetime import datetime


class mainClass():

    def __init__(self):
        super().__init__()
        subprocess.check_output("adb devices")

    def screenshot(self,path):
        try:
            subprocess.run(f"adb shell screencap -p > {path}", check=True, timeout=5)
            return True

        except Exception as e:
            raise e

    def videoStart(self,filename):
        try:
            global TS1
            global rec
            TS = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.mp4')
            TS1 = filename+TS
            command = ['adb', 'shell', 'screenrecord', '//sdcard/' +TS1]

            rec = subprocess.Popen(command)
            print("video recording started")

        except Exception as e:
            raise e

    def videoStop(self, d_path):
        try:
            rec.terminate()
            time.sleep(2)
            cmd = ['adb', 'pull', 'sdcard/' + TS1, f'{d_path}']
            subprocess.run(cmd)
            print("video captured")

        except Exception as e:
            raise e

    def startlog(self,filepath,filename):
        global b
        b = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")+'.txt')
        filepath = filepath+"\\"+filename+b
        try:
            with open(filepath, 'w+') as f:
                global pid
                pid = subprocess.Popen("adb logcat", stdout=f, text=True)
                f.write(filepath)
                f.seek(0)
                f.read()
                print("log capturing")
                f.close()

        except Exception as e:
            raise e

    def stoplog(self):
        try:
            pid.terminate()
            print("log captured")

        except Exception as e:
            raise e


class basicKeywords(mainClass):

    def __int__(self):
        pass

    def install(self,apkname):
        try:
            subprocess.check_output(['adb', 'install', apkname])
        except Exception as e:
            raise e

    def unistall(self,packageName):
        try:
            subprocess.run(['adb', 'uninstall', packageName])

        except Exception as e:
            raise e

    def launchapp(self,apkname):
        try:
            subprocess.check_output(['adb', 'shell', 'am', 'start', '-n', apkname])
            print("apk started sucessfully")

        except Exception as e:
            raise e

    def mtCall(self,dev_id1,phnum):
        try:
            subprocess.run(['adb', '-s', dev_id1, 'shell', 'am', 'start',
                                     '-a', 'android.intent.action.CALL', '-d', 'tel:' + phnum])
            time.sleep(20)

        except Exception as e:
            raise e

    def ansCall(self,dev_id2):
        try:
            subprocess.run(['adb', '-s', dev_id2, 'shell', 'input', 'keyevent', "5"])
            time.sleep(30)

        except Exception as e:
            raise e

    def rejCall(self,dev_id):
        try:
            subprocess.check_output(['adb', '-s', dev_id, 'shell', 'input', 'keyevent', "6"])
            time.sleep(10)

        except Exception as e:
            raise e

    def browseUrl(self, url):
        try:
            res = subprocess.run(['adb', 'shell', 'am', 'start', '-a','android.intent.action.VIEW','-d', url])
            return str(res)

        except Exception as e:
            raise e

    def clickCoordinates(self,x,y):
        try:
            subprocess.call(['adb', 'shell', 'input', 'tap', x,y])
        except Exception as e:
            raise e

    def clickConnections(self):
        try:
            subprocess.call("adb shell input tap 440 847")
        except Exception as e:
            raise e

class settingsKeywrods(basicKeywords):

    def wifiOn(self):
        try:
            subprocess.run(['adb', 'shell', 'input', 'swipe','500','500','500','500'])  # swipe the screen
            subprocess.run(['adb', 'shell', 'svc', 'wifi','enable'])

        except Exception as e:
            raise e

    def wifiOff(self):
        try:
            subprocess.check_output(['adb', 'shell', 'svc', 'wifi','disable'])

        except Exception as e:
            raise e

    def btOn(self):
        try:
            # subprocess.run(['adb', 'shell', 'input', 'swipe', '500', '500', '500', '1000']) # swipe the screen
            # subprocess.check_output(['adb', 'shell', 'cmd', 'bluetooth_manager','enable'])
            subprocess.run("adb shell am start -a android.settings.BLUETOOTH_SETTINGS")
            subprocess.run("adb shell am start -a android.bluetooth.adapter.action.REQUEST_ENABLE")
            time.sleep(3)
            subprocess.run("adb shell input keyevent 22")
            subprocess.run("adb shell input keyevent 22")
            subprocess.run("adb shell input keyevent 66")

        except Exception as e:
            raise e


    def btOff(self):
        try:
            # subprocess.check_output(['adb', 'shell', 'cmd', 'bluetooth_manager','disable'])
            subprocess.check_output(['adb', 'shell', 'svc', 'bluetooth_manager', 'disable'])

        except Exception as e:
            raise e

    def locationOn(self):
        try:
            subprocess.run(['adb', 'shell', 'input', 'swipe', '500', '500', '500', '1000'])
            subprocess.run(['adb', 'shell', 'settings', 'put', 'secure', ',location_mode', '3'])

        except Exception as e:
            raise e

    def locationOff(self):
        try:
            subprocess.run(['adb', 'shell', 'settings', 'put', 'secure', ',location_mode', '0'])

        except Exception as e:
            raise e

    def aireplaneOn(self):
        try:
            subprocess.run(['adb', 'shell', 'input', 'swipe', '500', '500', '500', '1000'])
            subprocess.run(['adb', 'shell', 'settings', 'put', 'global', ',airplane_mode_on', '1'])

        except Exception as e:
            raise e

    def aireplaneOff(self):
        try:
            subprocess.run(['adb', 'shell', 'settings', 'put', 'global', ',airplane_mode_on', '0'])
        except Exception as e:
            raise e

    def dataOn(self):
        try:
            subprocess.run(['adb', 'shell', 'input', 'swipe', '500', '500', '500', '1000'])
            subprocess.run(['adb', 'shell', 'svc', 'data','enable'])

        except Exception as e:
            raise e

    def dataOff(self):
        try:
            subprocess.check_output(['adb', 'shell', 'svc', 'data','disable'])

        except Exception as e:
            raise e

class validationKeywrods(settingsKeywrods):

    def __int__(self):
        pass


    def btValidation(self):
        try:
            res = subprocess.check_output(['adb', 'shell', 'settings', 'get', 'global', 'bluetooth_on'],encoding="utf-8")
            return int(res)
        except Exception as e:
            raise e

    def wifiValidation(self):
        try:
            res = subprocess.check_output(['adb', 'shell', 'dumpsys', 'wifi', '|', 'grep', '\"Wi-Fi','is\"'],encoding="utf-8")
            #print(res)
            if "enabled" in str(res):
                print("wifi is on")
                return True

            else:
                print("wifi is off")
                return False

        except Exception as e:
            raise e

    def locationValidation(self):
        try:
            res = subprocess.check_output(['adb', 'shell', 'settings', 'get', 'secure', 'location_mode'],encoding="utf-8")
            if int(res) == 3:
                print("location is On")
                return True

            else:
                print("location is off")
                return False

        except Exception as e:
            raise e

    def dataValidation(self):
        try:
            res = subprocess.check_output(['adb', 'shell', 'settings', 'get', 'global', 'mobile_data'],encoding="utf-8")
            if int(res) == 0:
                print("mobile data is Off")
                return True

            else:
                print("mobile data is on")
                return False

        except Exception as e:
            raise e

    def aireplaneModeValidation(self):
        try:
            res = subprocess.check_output(['adb', 'shell', 'settings', 'get', 'global', 'airplane_mode_on'],encoding="utf-8")
            if int(res) == 0:
                print("aireplane Mode is Off")
                return True

            else:
                print("aireplane Mode is on")
                return False

        except Exception as e:
            raise e

class adbKeywords(validationKeywrods):

    def __int__(self):
        pass

    def homeKey(self):
        try:
            subprocess.run("adb shell input keyevent 3")
        except Exception as e:
            raise e

    def backKey(self):
        try:
            subprocess.run("adb shell input keyevent 4")
        except Exception as e:
            raise e