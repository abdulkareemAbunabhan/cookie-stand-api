from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CookieStand
from accounts.models import CustomUser

class CookiesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = CustomUser.objects.create_user(username='testuser1', password='pass')
        test_stand = CookieStand.objects.create(
            location='NewYork',
            owner=testuser1,
            description="Nothing",
            hourly_sales=30,
            minimum_customers_per_hour=5,
            maximum_customers_per_hour=10,
            average_cookies_per_sale=4
        )

    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username='test',
            email='test@email.com',
            password='1234'
        )

        self.cookie = CookieStand.objects.create(
            location='Delhi',
            owner=self.user,
            description='Something',
            hourly_sales=40,
            minimum_customers_per_hour=4,
            maximum_customers_per_hour=8,
            average_cookies_per_sale=8
        )

    def test_C_model(self):
        stand = CookieStand.objects.get(id=1)
        actual_owner = stand.owner.username
        actual_location = stand.location
        actual_description = stand.description
        actual_hourly_sales = stand.hourly_sales
        actual_minimum_customers_per_hour = stand.minimum_customers_per_hour
        actual_maximum_customers_per_hour = stand.maximum_customers_per_hour
        actual_average_cookies_per_sale = stand.average_cookies_per_sale

        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_location, "NewYork")
        self.assertEqual(actual_description, "Nothing")
        self.assertEqual(actual_hourly_sales, 30)
        self.assertEqual(actual_minimum_customers_per_hour, 5)
        self.assertEqual(actual_maximum_customers_per_hour, 10)
        self.assertEqual(actual_average_cookies_per_sale, 4)
