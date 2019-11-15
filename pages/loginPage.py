#Login test adımı
class LoginPage():

    def __init__(self, driver):
        self.driver = driver

#Kullanıcı adı ve parolanın alınarak girilmesi ve login butonuna tıklanması adımı

        self.username_textbox_id    = "idToken1"
        self.password_textbox_id    = "idToken2"
        self.login_button_id        = "loginButton_0"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_textbox_id).clear()
        self.driver.find_element_by_id(self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_textbox_id).clear()
        self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()
