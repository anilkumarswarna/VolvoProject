from LamdaAutomation.Utils import  followFriend
from LamdaAutomation.Library import uiLibrary
import time

aj1 = followFriend.followFriend()
aj2 = uiLibrary.uiLibrary()


aj2.launchApp("Instagram Lite")
time.sleep(4)
aj1.FollowFriendUi()
time.sleep(3)
aj1.Search()
time.sleep(4)
aj1.clickSearchUi()
time.sleep(5)
aj1.inputFriendADB()
time.sleep(6)
aj1.FollowFriendUi()
time.sleep(3)
aj1.backHomeUi()









