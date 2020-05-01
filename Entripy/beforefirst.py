class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.email_textbox_name = "model.Email"
        self.password_textbox_name = "model.Password"
        self.login_button_xpath = "//*[@id='login-form']/div/div/div[3]/input"

    def enter_email(self, email):
        self.driver.find_element_by_name(self.email_textbox_name).clear()
        self.driver.find_element_by_name(self.email_textbox_name).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element_by_name(self.password_textbox_name).clear()
        self.driver.find_element_by_name(self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()
