from yandex_testing_lesson import is_palindrome


def test_reverse():
    # Список тестов
    # Каждый тест — это пара (входное значение, ожидаемое выходное значение)
    test_data = (
        # неправильный тип входного аргумента, ни с чем не будем сравнивать
        (42, None),
        # тоже неправильный входной аргумент, но он "похож" на строку
        # (можно итерироваться и брать срезы)
        (['a', 'b', 'c'], None),
        # "граничный" случай — пустая строка
        ('', ''),
        # "особый" случай — строка, которая не меняется при разворачивании
        ('aba', 'aba'),
        # ещё один "особый" и почти "граничный" случай
        ('a', 'a'),
        # "обычный" случай
        ('abc', 'cba'),
    )

    for input_s, correct_output_s in test_data:
        try:
            output_s = is_palindrome(input_s)
        except Exception:
            print('NO')
            return False
        else:
            if output_s != correct_output_s:
                # если ответ не совпал с ожидаемым, завершаем тестирование и возвращаем False
                print('NO')
                return False
    # тестирование успешно пройдено
    print('YES')
    return True
