from django.conf import settings
from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
# TDD
User = get_user_model()
class OrderTestCase(TestCase):

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

    # def test_create_order(self):
    #     obj = Order.objects.create(user=self.user_a, product=product_a)
