from django.test import TestCase
from apps.newsletter.models import NewsLetter


class TestNewsLetterModel(TestCase):
    def setUp(self):
        self.newsletter = NewsLetter.objects.create(
            email="somemail@mail.com",
        )

    def test_models_dealer(self):
        self.assertIsNotNone(self.newsletter.id)
        self.assertEqual(self.newsletter.email, 'somemail@mail.com')