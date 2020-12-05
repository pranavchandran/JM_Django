from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
from .models import Product

User = get_user_model()

class ProductTestCase(TestCase):

    def setUp(self):
        user_a = User(username='kuttu', email='kuttu@gmail.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'kuttu'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = False
        user_a.set_password(user_a_pw)
        user_a.save()
        # import pdb; pdb.set_trace()
        # print(user_a.id)
        self.user_a = user_a
        user_b = User.objects.create_user('user_2', 'kuttu@gmail.com', 'kuttu_psw')
        user_a.is_staff = True
        self.user_b = user_b
        
    def test_user_count(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_invalid_request(self):
        self.client.login(username=self.user_b.username, password='kuttu_psw')
        # print(self.user_b.password)
        response = self.client.post("/products/create/",
        {"title":"this is an invalid test"})
        # print(response)
        self.assertTrue(response.status_code!=200) #302

    def test_valid_request(self):
        self.client.login(username=self.user_a.username, password='kuttu')
        # print(self.user_b.password)
        response = self.client.post("/products/create/",
        {"title":"this is an valid test"})
        print(response)
        self.assertTrue(response.status_code==200) #302

    def test_user_password(self):
        user_a = User.objects.get(username="kuttu")
        # import pdb; pdb.set_trace()
        # print(user_a)
        self.assertTrue(user_a.check_password(self.user_a_pw))

