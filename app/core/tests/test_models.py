from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_sucessful(self):
        """ Test creating a new user with email is sucessful """
        email = "test@gmail.com"
        password = "test@1234"

        user = get_user_model().objects.create_user(
        email=email,
        password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
