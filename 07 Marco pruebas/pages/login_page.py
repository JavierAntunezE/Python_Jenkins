
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:

    def __init__(self, driver): #Constructor
        #Guarda el driver como atributo interno, para que todos los métodos de la clase puedan usarlo
        self.driver = driver
        #define localizadores como una tupla(estrategia, valor)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "h3[data-test='error']")

    def wait_until_loaded(self, timeout=10): #Verifica que los elementos estén presentes o visibles
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.username_input)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(self.password_input)
        )
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(self.login_button)
        )

    def enter_username(self, username):
        #El * descompone la tupla en dos argumentos: By.ID, "user-name".
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
