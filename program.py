from yandex_testing_lesson import is_palindrome


def test_reverse():
    test_data = (
        ('', True),
        ('aba', True),
        ('a', True),
        ('abc', False),
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
