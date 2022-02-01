from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from authentication.models import OneTimePassword


class TestAuthentication(TestCase):
    def setUp(self):
        self.client = Client()

        self.test_user = User.objects.create(username='testuser', password='123456', email='test@test.com')
        self.test_user.is_staff = True
        self.test_user.save()
        self.test_otp1 = OneTimePassword.objects.create(user=self.test_user, otp=2222)
        self.test_otp1.save()

        self.test_user2 = User.objects.create(username='testuser2', password='123456')
        self.test_user2.save()

        self.login_url = reverse('login_page')
        return super().setUp()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get('/aqajbl/')
        self.assertRedirects(response, '/levdbt/?next=/aqajbl/')

    def test_can_access_page(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin/login.html')

    def test_login_staff(self):
        response = self.client.post(self.login_url, username=self.test_user.username, password='123456',
                                    format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_login_not_staff(self):
        response = self.client.post(self.login_url, username=self.test_user2.username, password='123456',
                                    format='text/html')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login_page'), status_code=302,
                             target_status_code=200)

    def test_login_wrong_password(self):
        response = self.client.post(self.login_url, username=self.test_user2.username, password='654321',
                                    format='text/html')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login_page'), status_code=302,
                             target_status_code=200)

    def test_otp_redirect(self):
        response = self.client.post(self.login_url, username=self.test_user.username, password='123456',
                                    format='text/html')
        self.assertRedirects(response, reverse('login_page'), status_code=302,
                             target_status_code=200)

    def test_otp_pass(self):
        response = self.client.post(reverse('check_otp', kwargs={'email': self.test_user.email}), {'otp': 2222},
                                    format='text/html')
        self.assertRedirects(response, '/aqajbl/')

    def test_opt_wrong(self):
        response = self.client.post(reverse('check_otp', kwargs={'email': self.test_user.email}), {'otp': 5555},
                                    format='text/html')
        self.assertRedirects(response, reverse('login_page'), status_code=302,
                             target_status_code=200)


