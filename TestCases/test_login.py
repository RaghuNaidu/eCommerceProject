from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):
        self.logger.info(" *********Test_001_Login******** ")
        self.logger.info(" *********Verfifying Home page title******** ")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("*********Home page title test is PASSED********")
        else:
            self.driver.save_screenshot(".//ScreenShots//" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.error("*********Home page title test is FAILED********")
            assert False

    def test_login(self, setup):
        self.logger.info("*********Verifying the login test********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*********Login test is PASSED********")
            self.driver.close()
        else:
            self.driver.save_screenshot(".//ScreenShots//" + "act_title.png")
            self.driver.close()
            self.logger.error("*********Login test is FAILED********")
            assert False
