"""
Параметризация автотестов.
Тестирует endpoints API работы с пропусками на автомашины (на КАД и т.д.)
на корректный ответ, когда пользователь не авторизован
Tests vehicle pass API endpoints (for KAD, etc.)
for correct unauthorized response
Автор: Евгений Петров (Eugenii Petrov)
E-mail: p174@mail.ru
Phone: +7 952 517 4228
"""

import unittest
from typing import Callable

import requests
from requests import Response


class TestingEndpoints(unittest.TestCase):
    """
    Тестирует endpoints API работы с пропусками на автомашины (на КАД и т.д.)
    на корректный ответ, когда пользователь не авторизован
    Tests vehicle pass API endpoints (for KAD, etc.)
    for correct unauthorized response

    Args:
        unittest (_type_): _description_
    """

    #  Выводим в случае ответа, отличного от Unauthorized
    #  Show if the response is not Unauthorized
    _ERR_UNAUTH_MSG: str = 'Ожидается "Unauthorized", получено'

    #  Базовый URL тестируемого API
    #  Base URL of the API being tested
    _BASE_TESTING_URL = "https://tanos-cp.dt-teh.ru/api/passes/v1"

    def _check_authorization(self, response: Response) -> None:
        """
        Проверяет на корректность ответа. Ожидаю ошибку 401
        Validates response correctness. Expects 401 error
        """

        err_msg = (
            f"Неверные данные ответа, ожидается 401:{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

    def _check_message_key(self, response_data: Response) -> None:
        """
        Проверяю наличие обязательного ключа в ответе
        Проверяю ключ "message"
        Verify the presence of mandatory key 'message' in the response
        """

        self.assertIn(
            "message",
            response_data,
            'Ключ "message" не найден в ответе от сервера',
        )


def create_test_factory(
    line: str,
) -> Callable[[unittest.TestCase], None]:
    """Фабрика тестовых методов"""

    def test_factory(self) -> None:
        """
        Тeстирую заданный эндпоинт
        """
        # print(line.strip())
        response: Response = requests.get(line.strip("\n\r"))
        self._check_authorization(response)
        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response.json()["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    return test_factory


def sanitize_identifier(text: str) -> str:
    """
    Убираю все символы, не подходящие в имени метода
    Removing all invalid method name characters
    """
    cleaned = "".join(c for c in text if c.isidentifier() or c.isdigit())
    while cleaned and cleaned[0].isdigit():
        cleaned = cleaned[1:]
    return cleaned or "_"


with open("endpoints_to_test.tst") as endpoints_file:
    line: str = ""
    for line in endpoints_file:
        # print(line)
        clean_line = sanitize_identifier(line)
        #  Не забываем написать test_ !!!!
        #  Иначе тест не будет запущен!
        test_name = f"test_{clean_line}"
        test_method = create_test_factory(line)
        setattr(TestingEndpoints, test_name, test_method)

if __name__ == "__main__":
    unittest.main()
