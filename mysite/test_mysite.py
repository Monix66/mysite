from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json',]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        # opts.headless = True # DEPRECATED!
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        # No cerramos el navegador para verificar visualmente lo que sucedió
        # cls.selenium.quit()
        super().tearDownClass()

    def create_sample_page(self):
        # Crea una página sencilla en el raíz
        from django.core.management import call_command
        call_command('create_sample_page')

    def test_login_and_view_site_button(self):
        # Crear una página sencilla si no existe en el raíz
        self.create_sample_page()

        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))

        # Comprobar que el título de la página es el esperado
        self.assertEqual(self.selenium.title, "Log in | Django site admin")

        # Introducir datos de inicio de sesión y hacer clic en el botón "Log in"
        username_input = self.selenium.find_element(By.NAME, "username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element(By.NAME, "password")
        password_input.send_keys('admin123')
        password_input.send_keys(Keys.RETURN)

        # Comprobar que hemos entrado al panel de administración por el título
        self.assertEqual(self.selenium.title, "Site administration | Django site admin")

        # Asegurarnos de que existe el botón "View Site"
        view_site_button = self.selenium.find_element(By.XPATH, "//a[text()='View site']")
        self.assertIsNotNone(view_site_button)

        # Hacer clic en el botón "View Site"
        view_site_button.click()

        # Comprobar que la página a la que se accede tiene un código de respuesta 200
        self.assertEqual(self.selenium.title, "Your Sample Page Title")  # Reemplazar con el título real de tu página
