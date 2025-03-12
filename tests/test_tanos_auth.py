"""
Тестирование endpoints с авторизацией
"""

import errno
import json
import logging
import unittest
from typing import Optional

import requests
from requests import Response

import settings_local

user_name: str = settings_local.user1
password: str = settings_local.password1
logging.basicConfig(level=logging.DEBUG)


def get_value_from_json(json_date, key):
    data = json.loads(json_date)
    return data.get(key)


class TestAytorizedAccess(unittest.TestCase):
    token: str | None = None

    @classmethod
    def setUpClass(cls):
        cls.api_url: str = ""
        """
        Тестирую  url https://tanos-cp.dt-teh.ru/api/passes/v1/list
        Базовые настройки
        """
        cls.auth_url: str = "https://tanos-cp.dt-teh.ru/api/token/pair"
        cls.auth_payload: dict = {"phone": user_name, "password": password}
        cls.token = cls.get_bearer_token()

    @classmethod
    def get_bearer_token(cls) -> str | None:
        """
        Получение токена авторизации
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
        self.assertIsNotNone(self.token, "Токен не найден в ответе.")
        self.token: str | None = self.__class__.token
        self.api_url: str = self.__class__.api_url

    def test_auth_acces_pas_list(self):
        """
        Проверяю возвращаемые ключи
          в эндпоинте https://tanos-cp.dt-teh.ru/api/passes/v1/list
        """
        headers: dict = {"Authorization": f"Bearer {self.token}"}
        response: Response | None = None
        try:
            response = requests.get(self.api_url, headers=headers, timeout=5)
            err_msg = (
                f"Ошибка при запросе, код: {response.status_code} \n"
                f"json Ответа: {response.json()} "
            )
            self.assertEqual(response.status_code, 200, err_msg)

            car_id_present: int = 0
            car_id_present = sum(
                "car_id" in item for item in response.json()["items"]
            )
            self.assertTrue(car_id_present, "Ключ 'car_id' не найден в ответе")
            err_msg = (
                f"Ключ 'car_id' найден в {car_id_present} "
                f"элементах из {len(response.json()['items'])} "
            )
            logging.error(err_msg)

            for item in response.json()["items"]:
                logging.debug(item)
                car_id_data = item
                err_msg = f"Значение {car_id_data} должно быть integer"
                self.assertIsInstance(car_id_data, int, err_msg)

            reg_num_present: int = 0
            reg_num_present = sum(
                "reg_num" in item for item in response.json()["items"]
            )
            err_msg = "Ключ 'reg_num' не найден в ответе"
            self.assertTrue(reg_num_present, errno)
            info_msg = (
                f"Ключ 'reg_num' найден в {reg_num_present} "
                f"элементах из {len(response.json()['items'])} "
            )
            logging.debug(info_msg)

        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")

    def test_auth_pass_app_list(self):
        """
        Проверяю возвращаемые ключи в эндпоинтеhttps://tanos-cp.dt-teh.ru/api/passes/v1/application/list

        """
        self.api_url = "https://tanos-cp.dt-teh.ru/api/passes/v1/application/list?company_id=6000000"
        headers: dict = {"Authorization": f"Bearer {self.token}"}
        response: Response | None = None
        try:
            response = requests.get(self.api_url, headers=headers, timeout=5)
            err_msg = (
                f"Ошибка при запросе, ожидается код ответа 200 \n"
                f"Код: {response.status_code} \n "
                f"json Ответа: {response.json()}"
            )
            self.assertEqual(response.status_code, 200, err_msg)
        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")


if __name__ == "__main__":
    unittest.main()
