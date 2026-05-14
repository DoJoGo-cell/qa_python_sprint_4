# qa_python_4 - Books Collector

Проект содержит класс `BooksCollector` для управления коллекцией книг с жанрами

## Реализованные тесты (17 тестов):

### 1. Добавление новых книг
- `test_add_new_book_add_one_book_with_positive_value` — добавление книги с корректным названием (параметризованный тест: 2 названия)
- `test_add_new_book_add_two_books_with_same_names` — попытка добавить две книги с одинаковыми названиями
- `test_add_new_book_with_negative_value_long_name` — попытка добавить книги с некорректным названием (параметризованный тест: 2 названия)

### 2. Установка жанра книги
- `test_set_book_genre_set_genre_for_added_book` — установка жанра для существующей книги
- `test_set_book_genre_set_nonexistent_genre` — установка несуществующего жанра (жанр не сохраняется)

### 3. Получение жанра книги
- `test_get_book_genre_for_added_book` — получение жанра для существующей книги
- `test_get_book_genre_for_nonexistent_book_returns_none` — получение жанра для несуществующей книги (возвращает None)

### 4. Фильтрация книг по жанру
- `test_get_books_with_specific_genre_for_genre_fantastic` — получение всех книг определённого жанра (фантастика)
- `test_get_books_genre_for_empty_list` — получение словаря жанров для пустой коллекции

### 5. Получение списка детских книг
- `test_get_books_for_children_with_positive_value` — книги с допустимыми жанрами (Комедии, Фантастика, Мультфильмы) попадают в детский список (параметризованный тест: 3 книги)
- `test_get_books_for_children_with_negative_value` — книги с запрещёнными жанрами (Ужасы, Детективы) не попадают в детский список (параметризованный тест: 2 книги)

### 6. Избранное
- `test_add_book_in_favorites_for_book_in_list` — добавление существующей книги в избранное
- `test_add_book_in_favorites_for_book_not_in_list` — попытка добавить несуществующую книги в избранное
- `test_delete_book_from_favorites_for_books_are_inside` — удаление книги из избранного
- `test_get_list_of_favorites_books_for_empty_list` — получение списка избранного для пустой коллекции

## Запуск тестов
pytest -v tests.py

## Результат
17 passed in 0.05s

