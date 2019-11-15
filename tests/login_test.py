#Python'a gerekli modüllerin import edildiği alan
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.loginPage import LoginPage2
from pages.homePage import HomePage
from utils import utils as utils
import allure
import moment

#conftest.py sayfasından driver bilgilerini alan pytest tanımı
@pytest.mark.usefixtures("test_setup")
#class tanımı ile login ve home sayfalarındaki fonsiyonlar çağırılır.
class TestLogin():
    #Login test fonsiyonu (URL 1 için)
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    #Log out test fonsiyonu (URL 1 için)
    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_avatar()
            homepage.click_logout()
            title = driver.title
            # Yakalanan title ile tanımlı title eşleşmez ise exception alınarak aşağıdaki durumlar kotrol edilir.
            assert title == 'Solvay (Login)'

        #Ekran görüntüsü alınarak zaman ve tarih imzası ve fonsiyon adı ile kaydedilir.
        except AssertionError as error:
            print("Assertion error accurred")
            print(error)
            currentTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("D:/SSO/Lirex-Solvay/Lirex Selenium Tests/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was an exception")

            currentTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("D:/SSO/Lirex-Solvay/Lirex Selenium Tests/screenshots/" + screenshotName + ".png")

        else:
            print("No exceptions accurred")

        finally:
            print("Finally Login block")

    # Login test fonsiyonu (URL 2 için)
    def test_login2(self):
        driver = self.driver
        driver.get(utils.URL2)

        login = LoginPage2(driver)
        login.enter_username(utils.USERNAME2)
        login.enter_password(utils.PASSWORD2)
        login.click_login()

    #Log out test fonsiyonu (URL 2 için)
    def test_logout2(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_avatar()
            homepage.click_logout()
            title = driver.title
            # Yakalanan title ile tanımlı title eşleşmez ise exception alınarak aşağıdaki durumlar kotrol edilir.
            assert title == 'Solvay (Login)'

        #Ekran görüntüsü alınarak zaman ve tarih imzası ve fonsiyon adı ile kaydedilir.
        except AssertionError as error:
            print("Assertion error accurred")
            print(error)
            currentTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("D:/SSO/Lirex-Solvay/Lirex Selenium Tests/screenshots/" + screenshotName + ".png")
            raise

        except:
            print("There was an exception")

            currentTime = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName + "_" + currentTime
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshotName,
                          attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("D:/SSO/Lirex-Solvay/Lirex Selenium Tests/screenshots/" + screenshotName + ".png")

        else:
            print("No exceptions accurred")

        finally:
            print("Finally Login block")
