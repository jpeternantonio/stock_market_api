from django.test import TestCase, Client
from django.urls import reverse
from account.models import User


class TestAccountViews(TestCase):
    
    def setUp(self) -> None:
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
  

    def test_register_GET(self) -> bool:
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/register.html')


    def test_login_GET(self) -> bool:
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_logout(self) -> bool:
        user = User.objects.create_user('john', 'johndoe@gmail.com', 'Test456.')
        self.client.login(username='john', password='Test456.')
        response = self.client.get('/account/logout')
        self.assertEquals(response.status_code, 301)


