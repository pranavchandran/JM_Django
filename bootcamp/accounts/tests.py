from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
# TDD
User = get_user_model()
class UserTestCast(TestCase):

    def setUp(self):
        user_a = User(username='kuttu', email='kuttu@gmail.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'kuttu'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.set_password(user_a_pw)
        user_a.save()
        # import pdb; pdb.set_trace()
        # print(user_a.id)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        # user_qs = User.objects.filter(username__iexact="kuttu")
        # user_exists = user_qs.exists() and user_qs.count() == 1
        # self.assertTrue(user_exists)
        # user_a = user_qs.first()
        self.assertTrue(self.user_a.check_password('kuttu'))

    def test_login_url(self):
        # 'login_url = "/login"
        # self.assertEqual(settings.LOGIN_URL, login_url)
        login_url = settings.LOGIN_URL
        # print(login_url)
        # python requests- manage.py runserver
        # self.client.get, self.client.post
        # response = self.client.post(url, data, follow=True)
        data = {"username":"kuttu", "password": self.user_a_pw}
        response = self.client.post(login_url, data, follow=True)
        print(response.request)
        # print(dir(response))
        # print(type(response))
        # print(response.status_code)
        status_code = response.status_code
        redirect_path = response.request.get('PATH_INFO')
        # print(redirect_path)
        self.assertEqual(redirect_path, settings.LOGIN_URL)
        self.assertEqual(status_code, 200)


