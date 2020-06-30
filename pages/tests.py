from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

class HomepageViewTest(SimpleTestCase):
    def test_url(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)

    def test_url_by_name(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed('home.html')

class SignupViewTest(TestCase):
    username = 'sam'
    email = 'email@test.com'

    def test_signup_page(self):
        res = self.client.get('/users/signup/')
        self.assertEqual(res.status_code, 200)

    def test_signup_page_namespace(self):
        res = self.client.get(reverse('signup'))
        self.assertEqual(res.status_code, 200)
    
    def test_template(self):
        self.assertTemplateUsed('signup.html')

    def test_data_set(self):
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
