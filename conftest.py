import pytest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager

#Bu fonksiyon cmd üzerinde --browser parametresi ile browser seçme imkanı sağlar.
#Eğer herhangi bir parametre girilmez ise default olarak ilk browser ile çalışır.
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser e.g. chrome or firefox")

#login_test sayfasındaki driver bilgisi bu fonksiyon ile gönderilir.
@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.firefox.options import Options

    #--browser parametresi boş bırakılırsa default olarak Chrome ile çalışır.
    browser = request.config.getoption("--browser")
    if browser == 'explorer':
        caps = webdriver.DesiredCapabilities.INTERNETEXPLORER
        caps["ignoreProtectedModeSettings"] = True
        iepath = "D:/SSO/Lirex-Solvay/WebdriverManagerTest/drivers/IEDriverServer.exe"
        driver = webdriver.Ie(executable_path=iepath, desired_capabilities=caps)
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Ie(IEDriverManager().install())
    elif browser == 'firefox':
        fpath = "D:/SSO/Lirex-Solvay/Lirex Selenium Tests/drivers/geckodriver.exe"
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(executable_path= fpath, options= options)
        #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

    else:
        cpath = "D:/SSO/Lirex-Solvay/Lirex Selenium Tests/drivers/chromedriver.exe"
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path= cpath)
        #driver = webdriver.Ie(IEDriverManager().install())
        #driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

    print("Test Completed!")