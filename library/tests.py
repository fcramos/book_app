from django.test import TestCase
from datetime import datetime
from library.models import Author, Category, Book


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


class BookTest(TestCase):
    def setUp(self):
        self.author = Author(
            name='John Doe'
        )
        self.author.save()

        self.category = Category(
            description='Comedy',
        )
        self.category.save()

        self.book = Book(
            title='Any book',
            author=self.author,
            category=self.category,
            pages=900,
            description='',
            published_in=datetime.today()
        )
        self.book.save()

    def test_create(self):
        'Book instance may be saved'
        self.assertEqual(1, self.book.pk)

    def test_str(self):
        'Book string representation may be the name.'
        self.assertEqual('Any book', str(self.book))
