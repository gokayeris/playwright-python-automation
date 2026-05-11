class LoginPage:
    def __init__(self, page):
        self.page = page
        # Definimos los selectores como atributos de la clase
        self.username_input = page.get_by_placeholder("Username")
        self.password_input = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.error_message = page.locator("[data-test='error']")

    def navegar(self):
        self.page.goto("https://www.saucedemo.com/")

    def realizar_login(self, usuario, clave):
        self.username_input.fill(usuario)
        self.password_input.fill(clave)
        self.login_button.click()
