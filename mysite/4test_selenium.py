from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['testdb.json',]
 
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        opts = Options()
        #opts.headless = True # DEPRECATED!
        cls.selenium = WebDriver(options=opts)
        cls.selenium.implicitly_wait(5)
 
    @classmethod
    def tearDownClass(cls):
        # no sortim el browser per comprovar visualment com ha anat
        #cls.selenium.quit()
        super().tearDownClass()
 
    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/'))
        
        # comprovem que el títol de la pàgina és el què esperem
        self.assertEqual( self.selenium.title , "Log in | Django site admin" )
        
        # introduïm dades de login i cliquem el botó "Log in" per entrar
        username_input = self.selenium.find_element(By.NAME,"username")
        username_input.send_keys('admin')
        password_input = self.selenium.find_element(By.NAME,"password")
        password_input.send_keys('admin123')
        self.selenium.find_element(By.XPATH,'//input[@value="Log in"]').click()
        
        # comprovem que hem entrat al panell d'administració pel títol
        self.assertEqual( self.selenium.title , "Site administration | Django site admin" )
        
        # Aquesta localització de l'element ens serveix també a mode de ASSERT
        # Si no localitza el link "Log out", ens donarà un NoSuchElementException
        self.selenium.find_element(By.XPATH,"//button[text()='Log out']")