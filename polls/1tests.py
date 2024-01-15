from django.test import TestCase
from django.urls import reverse

# Aquest és el model de User habitual en un projecte estàndard
from django.contrib.auth.models import User
# Aquest altre és el model alternatiu quan tenim un User personalitzat
#from django.contrib.auth import get_user_model
#User = get_user_model()

class LoginTests(TestCase):
    def test_create_superuser(self):
        # Creem un superusuari
        User.objects.create_superuser('admin', 'admin@borsa.com', 'admin123')
        # ens loguem amb username (o amb email, segons es configuri)
        login = self.client.login(username='admin',password='admin123')
        self.assertTrue(login)
        # visitem la pàgina principal del panell de control /admin
        response = self.client.get('/admin/')
        # comprovem que el login és correcte si apareix "Benvingut/da" al HTML
        self.assertTrue( "Welcome" in str(response.content) )
        self.assertTrue( "Log out" in str(response.content) )

    def test_segon(self):
        # el superusuari creat al test anterior aquí ja no existeix
        # aquesta sentència fallarà
        login = self.client.login(username='admin',password='admin123')
        # no fem assertTrue de "login" per no provocar un test fallit
