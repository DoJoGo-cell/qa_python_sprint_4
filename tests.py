import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.mark.parametrize('book_name', [
        'Гордость и предубеждение и зомби',
        'Что делать, если ваш кот хочет вас убить'
    ])
    def test_add_new_book_add_one_book_with_positive_value(self,book_name):
        collector = BooksCollector()

        collector.add_new_book(book_name)

        assert book_name in collector.get_books_genre()

    def test_add_new_book_with_negative_value_long_name(self):
        collector = BooksCollector()

        result = collector.add_new_book('Что делать, если ваш кот хочет вас убить........?')

        assert 'Что делать, если ваш кот хочет вас убить........?' not in collector.get_books_genre()

    def test_set_book_genre_set_genre_for_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Фантастика'

    def test_set_book_genre_set_nonexistent_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Романтика')

        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_get_book_genre_for_added_book(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        result = collector.get_book_genre('Гордость и предубеждение и зомби')

        assert result == 'Фантастика'

    def test_get_book_genre_for_nonexistent_book_returns_none(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')

        result = collector.get_book_genre('Дюна')

        assert result is None

    def test_get_books_with_specific_genre_for_genre_fantastic(self):
        collector = BooksCollector()

        books_data = [
            ['Автостопом по галактике', 'Фантастика'],
            ['Дюна', 'Фантастика'],
            ['Винни-Пух', 'Мультфильм']
        ]

        for book_name, genre in books_data:
            collector.add_new_book(book_name)
            collector.set_book_genre(book_name, genre)

        fantastic_genre = collector.get_book_genre('Автостопом по галактике')
        result = collector.get_books_with_specific_genre(fantastic_genre)

        assert result == ['Автостопом по галактике', 'Дюна']

    def test_get_books_genre_for_empty_list(self):
        collector = BooksCollector()

        assert collector.get_books_genre() == {}

    @pytest.mark.parametrize('book_name, genre', [
        ['Горько', 'Комедии'],
        ['Дюна', 'Фантастика'],
        ['Винни-Пух', 'Мультфильмы']
    ])
    def test_get_books_for_children_with_positive_value(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        result = collector.get_books_for_children()

        assert book_name in result

    @pytest.mark.parametrize('book_name, genre', [
        ['Оно', 'Ужасы'],
        ['Шерлок Холмс', 'Детективы']
    ])
    def test_get_books_for_children_with_negative_value(self, book_name, genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)

        result = collector.get_books_for_children()

        assert book_name not in result


    def test_add_book_in_favorites_for_book_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')

        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        assert  'Гордость и предубеждение и зомби' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_for_books_are_inside(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')

        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')

        assert 'Гордость и предубеждение и зомби' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_for_empty_list(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []