"""
Тестирование endpoints с авторизацией
"""

import unittest
import json

import requests
from requests import Response

import settings_local

user_name: str = settings_local.user1
password: str = settings_local.password1


def get_value_from_json(json_date, key):
    data = json.loads(json_date)
    return data.get(key)


class TestAytorizedAccess(unittest.TestCase):
    def setUp(self):
        """
        Тестирую  url https://tanos-cp.dt-teh.ru/api/passes/v1/list
        Базовые настройки
        """
        self.auth_url: str = "https://tanos-cp.dt-teh.ru/api/token/pair"
        self.api_url: str = "https://tanos-cp.dt-teh.ru/api/passes/v1/list?company_id=0"
        self.auth_payload: dict = {
            'phone' : user_name,
            'password' : password
        }
        self.token: str|None = None
        self.token = self.get_bearer_token()


    def get_bearer_token(self):
        """
        Получение токена авторизации
        """
        try:
            responce: Response = requests.post(self.auth_url,
                                               json = self.auth_payload,
                                               timeout = 5)
            responce.raise_for_status()
            token: str|None = responce.json().get("access")
            self.assertIsNotNone(token,
                                  "Токен не найден в ответе.")
            print(token)
            return token

        except requests.exceptions.RequestException as err :
            self.fail (f"Ошибка при получении токена {err} ")


    def test_auth_acces_passes_list(self):
        """
        Проверяю возвращаемые ключи в эндпоинте https://tanos-cp.dt-teh.ru/api/passes/v1/list 
        """
        headers: dict = {'Authorization' : f'Bearer {self.token}'}
        try:
            response: Response = requests.get(self.api_url,
                                            headers = headers,
                                            timeout = 5)
            self.assertEqual(response.status_code,
                            200,
                            f"Ошибка при запросе, код: {response.status_code} \n json Ответа: {response.json()} ")
            car_id_present: int = 0
            car_id_present = sum( 'car_id' in item for item in response.json()['items'])
            self.assertTrue(car_id_present, "Ключ 'car_id' не найден в ответе")
            print(f"Ключ 'car_id' найден в {car_id_present} элементах из {len(response.json()['items'])} ")
            
            for item in response.json()['items']:
                print(item)
                # print(typeof(item))
                car_id_data = get_value_from_json(item, "car_id")
                self.assertIsInstance(car_id_data, int, f'Значение {car_id_data} должно быть integer')

            reg_num_present: int = 0
            reg_num_present = sum( 'reg_num' in item for item in response.json()['items'])
            self.assertTrue(reg_num_present, "Ключ 'reg_num' не найден в ответе")
            print(f"Ключ 'reg_num' найден в {reg_num_present} элементах из {len(response.json()['items'])} ")


        except requests.exceptions.RequestException as err:
            self.fail(f"\nОшибка при обращении к endpoint: {err}")


if __name__ == "__main__":
    unittest.main()