import subprocess
import time
from datetime import datetime


# mydata =  {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964 ,
#   "instagramPackageName" : "com.instagram.lite/com.facebook.lite.MainActivity"
# }

filename = "Phone storage/Videos/demo.mp4"
def videoStart(self,filename):

  global TS1
  global rec

  # TS = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + '.mp4')
  # TS1 = filename + TS
  command = ['adb', 'shell', 'screenrecord', '//Phone storage/Videos/demo.mp4/']

  rec = subprocess.Popen(command)
  # print("video recording started")


def videoStop(self, d_path):
  rec.terminate()
  time.sleep(2)
  cmd = ['adb', 'pull', 'Phone storage/' , f'{d_path}']
  subprocess.run(cmd)
  print("video captured")



videoStart(self=0, filename = "Phone storage")
videoStop(self=0,d_path="Phone storage")
