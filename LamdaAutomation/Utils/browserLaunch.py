from Library.browserLibrary import browserLibrary
import time
obj = browserLibrary()

class browserLaunch():

    def launchChrome(self):
        obj.launch_Chrome()

    def maxWindow(self):
        obj.max_Window()

    def openUrl(self):
        #Facebook
        obj.open_Url("https://www.facebook.com/",expRes="https://www.facebook.com/")
        #Letskodeit
        # obj.open_Url("https://www.letskodeit.com/practice",expRes="https://www.letskodeit.com/practice")

    def textVal_ByClsName(self):
        obj.text_val("_8eso","Facebook helps you connect and share with the people in your life.")

    def imgVal_ByClsName(self):
        obj.img_Val("_8ilh")

    def userName_ByID(self):
        obj.userName("email","anilkumarswarna158@gmail.com")
        # obj.userName("username-field","value")

    def password_BYName(self):
        obj.pssword("pass","SAnil@155","_9lsb")


    def password11(self):
        obj.password("password", "Password")


    def Button(self):
        obj.Button("login-form-submit")


    def clear_Text(self):
        obj.clear("email","pass")

    def forgot_Pass(self):
        obj.forgot_Pass("//a[text()='Forgotten password?']","Forgotten Password | Can't Log In | Facebook")

    def back(self):
        obj.back()

    def username(self):
        obj.clear("email","anilkumarswarna158@gmail.com")

    def password(self):
        obj.password("pass","SAni@155")

    def link_BY_Click(self):
        obj.link('Create a Page',expRes="https://www.facebook.com/pages/create/?ref_type=registration_form")


    def partail_Link_ByText(self):
        obj.partial_Link("Page")

    def input_start_with(self):
        obj.input_Starts_With('//*[starts-with(@id,"email")]',"starts-wtih@gmail.com")

    def OR_And(self):
        obj.OR_And("//input[@id='email1' or @class='inputtext _55r1 _6luy']","or@gmail.com","//input[@id='pass' and @name='pass']","and@gmail.com")

    def exit_allBrowsers(self):
        obj.exit()

    def click(self):
        obj.click("bmwradio")
        time.sleep(5)

    def chechBox(self):
        obj.check_Box("bmwcheck")

    def dropDown(self):
        obj.dropDown("carselect","//select[@id='carselect']")

    def implicit_wait(self):
        obj.implicit_wait()

    def windows_Handling(self):
        obj.manage_windows("openwindow",'//*[@id="navbar-inverse-collapse"]/div/div/a','bmwradio')

    def manage_Popups(self):
        obj.manage_Popups("//input[@id='alertbtn']","//input[@id='confirmbtn']","//input[@value='Login']")






