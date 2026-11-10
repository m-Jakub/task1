import unittest

from project.books.models import Book


def book(author):
    return Book(name='Test', author=author, year_published=2000, book_type='2days')


class TestAuthorValidation(unittest.TestCase):

    def test_poprawni_autorzy(self):
        for author in ['J.R.R. Tolkien', 'Józef Maria Bocheński',
                       'Antoine de Saint-Exupéry', "A'BC", 'Karol Wojtyła']:
            self.assertEqual(book(author).author, author)

    def test_niepoprawni_autorzy(self):
        for author in ['<script>alert(1)</script>', '<img src=x onerror=alert(1)>',
                       '', 'A' * 65]:
            with self.assertRaises(ValueError):
                book(author)

    def test_edycja_tez_walidowana(self):
        b = book('Karol Wojtyła')
        with self.assertRaises(ValueError):
            b.author = '<script>alert(1)</script>'


if __name__ == '__main__':
    unittest.main()
