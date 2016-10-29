from django.test import TestCase
from library.models import Author


class AuthorTest(TestCase):
    def setUp(self):
        self.author = Author(
            name='John Doe'
        )
        self.author.save()

    def test_create(self):
        'Author may be saved'
        self.assertEqual(1, self.author.pk)

    def test_str(self):
        'Author string representation may be the name.'
        self.assertEqual('John Doe', str(self.author))
