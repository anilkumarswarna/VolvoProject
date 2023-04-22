import time
import pytest


from Demo.Demo.resources.testdata import my_data

filePath = my_data["filepath"]

@pytest.mark.sanity
def test_bt(obj,launch_settings):
    obj.startlog(filePath,"test_bt_")
    obj.videoStart("test_bt_")
    time.sleep(2)
    obj.clickConnections()
    #Steps / Navigation
    btOnres = obj.btValidation() #logic validation
    obj.btOn()
    time.sleep(5)
    obj.btOff()
    btOffres = obj.btValidation() #logic validation
    obj.homeKey()
    # #Pyetst Validaiton
    assert btOnres == 1
    obj.stoplog()

@pytest.mark.regression
def test_wifi(obj,launch_settings):
    obj.startlog(filePath, "test_settingsLaunch_")
    obj.videoStart("test_settingsLaunch_")
    time.sleep(2)
    obj.clickConnections()

    obj.wifiOn()
    time.sleep(2)
    obj.wifiOff()

    time.sleep(2)
    obj.videoStop(filePath)
    obj.stoplog()



