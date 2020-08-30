from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account.views import register, user_login
from django.contrib.auth import views as auth_views


class TestUrls(SimpleTestCase):

    def test_register_url_is_resolved(self) -> bool:
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)


    def test_login_url_is_resolved(self) -> bool:
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, auth_views.LoginView)

    def test_login_url_is_resolved(self) -> bool:
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, auth_views.LogoutView)
