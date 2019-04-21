from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_create_user(self):
        email = "test@swapper.ru"
        password = "TestPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_email_normalize(self):
        email = 'test@SWAPPER.PW'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'testBest123')

    def test_creat_superuser(self):
        user = get_user_model().objects.create_superuser(
            email="test@super.com",
            password="pass123"
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
