from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTests(TestCase):
    def setUp(self):
        # Creem un superusuari vàlid per a tots els tests
        User.objects.create_superuser('admin', 'admin@borsa.com', 'admin123')
        # si ens loguem al setUp, també el client estarà logat per a tots els tests
        login = self.client.login(username='admin',password='admin123')
        self.assertTrue(login)

    def test_superuser(self):
        # visitem la pàgina principal del panell de control /admin
        response = self.client.get('/admin/')
        # comprovem que el login és correcte si apareix "Benvingut/da" al HTML
        self.assertTrue( "Welcome" in str(response.content) )

    def test_segon(self):
        # visitem la pàgina principal del panell de control /admin
        response = self.client.get('/admin/')
        # comprovem que el login és correcte si apareix el logout al HTML
        self.assertTrue( "Log out" in str(response.content) )