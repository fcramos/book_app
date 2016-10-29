from django.test import TestCase
from library.models import Author, Category


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


class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(
            description='Comedy'
        )
        self.category.save()

    def test_create(self):
        'Category instance may be saved.'
        self.assertEqual(1, self.category.pk)

    def test_str(self):
        'Category string representation may be the name.'
        self.assertEqual('Comedy', str(self.category))
