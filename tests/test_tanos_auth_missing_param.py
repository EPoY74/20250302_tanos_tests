"""
Тестирование endpoints с авторизацией, 
но без ввода обязательных параметров. 
Смотрим, что возврящается, если их не
"""

import json
import logging
from pickle import NONE
import unittest

import requests
from requests import JSONDecodeError, Response

import settings_local

user_name: str = settings_local.user1
password: str = settings_local.password1

logging.basicConfig(level=logging.DEBUG)


class TestAytorizedAccess(unittest.TestCase):
    """
    Класс для тесторования API с неуказанными обязательными параметрами
    """
    token: str | None = None


    @classmethod
    def setUpClass(cls) -> None:
        """
        Тестирую  url https://tanos-cp.dt-teh.ru/api/passes/v1/list
        Базовые настройки для всего класса 
        """
        cls.api_url: str = ""
        cls.auth_url: str = "https://tanos-cp.dt-teh.ru/api/token/pair"
        cls.auth_payload: dict = {"phone": user_name, "password": password}
        cls.token = cls.get_bearer_token()


    @classmethod
    def get_bearer_token(cls) -> str | None:
        """
        Получение токена авторизации один раз для всего класса
        Returns:
            str: Токен авторизации, если запрос успешен.
            None: В случае ошибки (например, сетевой проблемы или невалидного ответа).
        """
        try:
            response: Response = requests.post(
                cls.auth_url, json=cls.auth_payload, timeout=5
            )
            response.raise_for_status()
            token = response.json().get("access")
            logging.debug(token)
            return token
        except json.JSONDecodeError as err:
            logging.error(f"Ошибка получения токена: {err}")
            return None
        except requests.exceptions.RequestException as err:
            logging.error(f"Ошибка при получении токена {err} ")
            return None
        except ValueError as err:
            logging.error(f"Ошибка обработки JSON: {err}")
            return None
         


    def setUp(self) -> None:
        """
        Вызавается перед каждым методом
        """
        super().setUp()
        try:
            self.assertIsNotNone(self.token, "Токен не найден в ответе.")
            self.token: str | None = self.__class__.token
            self.api_url: str = self.__class__.api_url
        except AttributeError as err:
            logging.error(f"Атрибут не найден: {err}")
            self.fail(f"Атрибут не найден: {err}")
        except requests.exceptions.RequestException as err:
            logging.error(f"Ошибка:  {err}")
            self.fail(f"Ошибка:  {err}")
        except Exception as err:
            logging.error(f"Непредвиденная ошибка: {err}")
            self.fail(f"Непредвиденная ошибка: {err}")    


    def test_auth_pass_list_missing(self) -> None:
        """
        Проверяю возвращаемые ключи в эндпоинте
        https://tanos-cp.dt-teh.ru/api/passes/v1/list
        В эндпоинте присутсвуют обязательные параметры.
        Проверяю, что бы не выдавалась информация, при
        отсутствии их.
        """
        response: Response | None = None
        headers: dict = {"Authorization": f"Bearer {self.token}"}
        self.api_url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/application/list"
        )
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
        except json.JSONDecodeError as err:
            logging.error(f"Ошибка json: {err}")
        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")
        except Exception as err:
            logging.error(f"Непредвиденная ошибка: {err}")
            self.fail(f"Непредвиденная ошибка: {err}") 


    def test_auth_pass_app_list_missing(self) -> None:
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
        except json.JSONDecodeError as err:
            logging.error(f"Ошибка json: {err}")
        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")
        except Exception as err:
            logging.error(f"Непредвиденная ошибка: {err}")
            self.fail(f"Непредвиденная ошибка: {err}") 


if __name__ == "__main__":
    unittest.main()
