from LamdaAutomation.Library import adbLibrary

obj = adbLibrary.adbLibrary()


class contactLibrary():

    def __init__(self):
        pass

    def launchContact(self):
        obj.launchApp("com.android.contacts/.activities.PeopleActivity")
    #
    # def pressBack(self):
    #     obj.pressBack()