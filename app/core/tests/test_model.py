from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


def sample_user(email='example@gmail.com', password='123456pass'):
    """Creates a sample user for tests"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a new user with an email is successful"""

        email = 'test@example.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_email_normalized(self):
        """Test that email for a new user is verified"""

        email = 'test@EXAMPLE.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, '1234rtes')

    def test_create_superuser(self):
        """Test creating new super user"""

        user = get_user_model().objects.create_superuser(
            'tests@gmail.com', '13144'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test tag string repr"""

        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEquals(str(tag), tag.name)
