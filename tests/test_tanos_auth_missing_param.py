"""
Тестирование endpoints с авторизацией
"""

import logging
import unittest

import requests
from requests import Response

import settings_local

user_name: str = settings_local.user1
password: str = settings_local.password1

logging.basicConfig(level=logging.DEBUG)


class TestAytorizedAccess(unittest.TestCase):
    token: str | None = None

    @classmethod
    def setUpClass(cls):
        cls.api_url: str = ""
        """
        Тестирую  url https://tanos-cp.dt-teh.ru/api/passes/v1/list
        Базовые настройки для для всего класса 
        """
        cls.auth_url: str = "https://tanos-cp.dt-teh.ru/api/token/pair"
        cls.auth_payload: dict = {"phone": user_name, "password": password}
        cls.token = cls.get_bearer_token()

    @classmethod
    def get_bearer_token(cls) -> str | None:
        """
        Получение токена авторизации один раз для всего класса
        """
        try:
            responce: Response = requests.post(
                cls.auth_url, json=cls.auth_payload, timeout=5
            )
            responce.raise_for_status()
            token = responce.json().get("access")
            logging.debug(token)
            return token

        except requests.exceptions.RequestException as err:
            logging.error(f"Ошибка при получении токена {err} ")
            return None

    def SetUp(self):
        """
        Вызавается перед каждым методом
        """
        self.assertIsNotNone(self.token, "Токен не найден в ответе.")
        self.token: str | None = self.__class__.token
        self.api_url: str = self.__class__.api_url

    def test_auth_pass_list_missing(self):
        """
        Проверяю возвращаемые ключи в эндпоинте
        https://tanos-cp.dt-teh.ru/api/passes/v1/list
        В эндпоинте присутсвуют обязательные параметры.
        Проверяю, что бы не выдавалась инфоормация, при
        отсутствии их. Привет для тестирования111

        """
        headers: dict = {"Authorization": f"Bearer {self.token}"}
        self.api_url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/application/list"
        )
        response: Response | None = None
        try:
            response = requests.get(self.api_url, headers=headers, timeout=5)
            self.assertEqual(
                response.status_code,
                400,
                (
                    f"Ошибка при запросе, код: {response.status_code} \n"
                    f"json Ответа: {response.json()}  "
                ),
            )

        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")

    def test_auth_pass_app_list_missing(self):
        """
        Проверяю возвращаемые ключи в эндпоинте
        https://tanos-cp.dt-teh.ru/api/passes/v1/application/list
        В эндпоинте присутсвуют обязательные параметры.
        Проверяю, что бы не выдавалась инфоормация, при
        отсутствии них.
        """
        self.api_url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/application/list"
        )
        headers: dict = {"Authorization": f"Bearer {self.token}"}
        response: Response | None = None
        try:
            response = requests.get(self.api_url, headers=headers, timeout=5)
            self.assertEqual(
                response.status_code,
                400,
                (
                    f"Ошибка при запросе, ожидается ошибка 400. \n"
                    f"Код: {response.status_code} \n"
                    f"json Ответа: {response.json()} "
                ),
            )

        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")


if __name__ == "__main__":
    unittest.main()
