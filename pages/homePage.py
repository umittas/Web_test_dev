#Log out sayfası adımları
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        #Logout fonsiyonu
        self.avatar_link_xpath = "//*[@id='loginContent']/li[2]/a"
        self.logout_link_xpath = "//*[@id='navDropdownMenu']/li[4]/a"

    def click_avatar(self):
        self.driver.find_element_by_xpath(self.avatar_link_xpath).click()

    def click_logout(self):
        self.driver.find_element_by_xpath(self.logout_link_xpath).click()