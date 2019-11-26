#Log out sayfası adımları
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        #Logout fonsiyonu
        self.welcome_link_id    = "welcome"
        self.logout_link_text   = "Logout"

    def click_avatar(self):
        self.driver.find_element_by_xpath(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_text).click()