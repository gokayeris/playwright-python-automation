from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("[data-test='username']")
        self.password_input = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")
        self.error_message = page.locator("[data-test='error']")

    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")

    def realizar_login(self, user, password):
        self.username_input.fill(user)
        self.password_input.fill(password)
        self.login_button.click()
