from LamdaAutomation.Library import uiLibrary
from LamdaAutomation.Library import adbLibrary

aj1 = uiLibrary.uiLibrary()
aj2 = adbLibrary.adbLibrary()


class followFriend():

    def FollowFriendUi(self):
        aj1.FollowFriendUI()

    def Search(self):
        aj1.SearchFriend()

    def clickSearchUi(self):
        aj1.TapfriendUI()

    def inputFriendADB(self):
        aj2.SeacrchFriendInput()

    def followFriend(self):
        aj1.FollowUI()

    def backHomeUi(self):
        aj1.pressBack()



    # def launchAppUI(q):
    #     q.d(text="Instagram Lite").click()
    #     time.sleep(2)
    #
    # #
    # def FollowFriendUI(self):
    #     self.d.click(300,1800)
    #     time.sleep(2)
    #
    # # S
    # def SearchFriend(self):
    #     self.d.click(900, 100)
    #     time.sleep(2)
    #     subprocess.run("adb shell input text 'Ella Vinay kumar'")
    #     time.sleep(3)
    #
    # # Click searched contact name
    # def TapfriendUI(self):
    #     self.d.click(100, 600)
    #     time.sleep(3)
    #
    #
    # def FollowUI(self):
    #     # self.d(className="android.view.ViewGroup", instance=4).click()
    #     self.d.click(200, 650)
    #     time.sleep(8)
    #
    # def SearchVideo(self):
    #     self.d.click(300,1800)
    #     time.sleep(2)
    # #
    # def VideoClickUI(self):
    #     self.d(className="android.view.ViewGroup",instance=5).click()
    #     time.sleep(4)
    #
    # def swipeADB1(self):
    #     subprocess.call("adb shell input swipe 400 1000 100 200")
    #
    # def SaveUI(self):
    #     # self.d(className="android.view.ViewGroup",instance=5).click()
    #     self.d.click(900,500)
    #
    #
    # def BackUI(self):
    #     for i in range(5):
    #         self.d.press.back()
