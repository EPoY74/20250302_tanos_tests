"""
Тестирование endpoints с авторизацией
"""

import unittest

import requests
from requests import Response

import settings_local

user_name: str = settings_local.user1
password: str = settings_local.password1


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
                                               timeout = 3)
            responce.raise_for_status()
            token: str|None = responce.json().get("access")
            self.assertIsNotNone(token,
                                  "Токен не найден в ответе.")
            return token

        except requests.exceptions.RequestException as err :
            self.fail (f"Ошибка при получении токена {err} ")
    
    # def test_print(self):
    #     print(str(self.token))
    def test_auth_acces_passes_list(self):
        """
        Проверяю возвращаемые ключи в эндпоинте https://tanos-cp.dt-teh.ru/api/passes/v1/list 
        """
        headers: dict = {'Authorization' : f'Bearer {self.token}'}
        try:
            response: Response = requests.get(self.api_url,
                                            headers = headers,
                                            timeout = 3)
            self.assertEqual(response.status_code,
                            200,
                            f"Ошибка при запросе, код: {response.status_code}")
            # self.assertIn("car_id",
            #             response.json()['items'],
            #             f"Ключ  car_id не найден в ответе.")
            car_id_present: int = 0
            car_id_present = sum( 'car_id' in item for item in response.json()['items'])
            self.assertTrue(car_id_present, "Ключ 'car_id' не найден в ответе")
            print(f"Ключ 'car_id' найден в {car_id_present} элементах из {len(response.json()['items'])} ")
        except requests.exceptions.RequestException as err:
            self.fail(f"Ошибка при обращении к защищенному endpoint {err}")


if __name__ == "__main__":
    unittest.main()