import unittest
import requests
from requests import Response


def sanitize_identifier(text):
    cleaned = "".join(c for c in text if c.isidentifier() or c.isdigit())
    while cleaned and cleaned[0].isdigit():
        cleaned = cleaned[1:]
    return cleaned or "_"


class TestingEndpoints(unittest.TestCase):
    """Тестирование endpoints API работы с пропусками на автомашины"""

    # Выводим в случае ответа, отличного от Unauthorized
    _ERR_UNAUTH_MSG: str = 'Ожидается "Unauthorized", получено'

    # Базовый URL тестируемого API
    _BASE_TESTING_URL = "https://tanos-cp.dt-teh.ru/api/passes/v1"

    def _check_authorization(self, response: Response) -> None:
        """Проверяет на корректность ответа. Ожидаю ошибку 401"""
        err_msg = (
            f"Неверные данные ответа, ожидается 401:{response.status_code}"
        )
        self.assertEqual(response.status_code, 401, err_msg)

    def _check_message_key(self, response_data: Response) -> None:
        """Проверяю наличие обязательного ключа в ответе"""
        self.assertIn(
            "message",
            response_data,
            'Ключ "message" не найден в ответе от сервера',
        )


def create_test_method(line):
    """Фабрика тестовых методов"""

    def test_method(self):
        """Тестирую заданный эндпоинт"""
        # print(line.strip())
        response = requests.get(line.strip("\n\r"))
        self._check_authorization(response)
        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{TestingEndpoints._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    return test_method


# Создаем тестовые методы для каждого endpoint
with open("endpoints_to_test.tst") as endpoints_file:
    for line in endpoints_file:
        clean_line = sanitize_identifier(line)
        test_name = f"test_{clean_line}"
        test_method = create_test_method(line)
        setattr(TestingEndpoints, test_name, test_method)


if __name__ == "__main__":
    unittest.main()
