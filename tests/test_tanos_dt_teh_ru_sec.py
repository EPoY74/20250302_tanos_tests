"""
Тестирует endpoints API пропусков на корректный ответ,
когда пользователь не авторизован
Testing if API endpoints respond correctly
to unauthenticated requests
"""

import unittest

import requests
from requests import Response


class TestUnautorezedAccessPassesV1(unittest.TestCase):
    """Тестирование API пропуска на корректный ответ, когда пользователь
    не авторизован.

    Args:
        unittest (_type_): _description_
    """

    #  Выводим в случае ответа, отличного от Unauthorized
    #  Show if the response is not Unauthorized
    _ERR_UNAUTH_MSG: str = 'Ожидается "Unauthorized", получено'

    #  Базовый URL тестируемого API
    #  Base URL of the API being tested
    _BASE_TESTING_URL = "https://tanos-cp.dt-teh.ru/api/passes/v1"

    def _check_authorisation(self, response: Response) -> None:
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

    def test_unauth_access_list(self):
        """
        Тестирование эндпоинта /list
        Endpoint testing: /list
        """
        url = self._BASE_TESTING_URL + "/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)
        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response.json()["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_app_list(self):
        """
        Тестирование эндпоинта /application/list
        Endpoint testing: /application/list
        """
        url = self._BASE_TESTING_URL + "/application/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_app_export(self):
        """
        Тестирование эндпоинта /application/export
        Endpoint testing: /application/export
        """
        url = self._BASE_TESTING_URL + "/application/export"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_allowed_zona_passes_list(self):
        """
        Тестирование эндпоинта /allowed-zona-passes/list
        Endpoint testing: /allowed-zona-passes/list
        """
        url = self._BASE_TESTING_URL + "/allowed-zona-passes/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_status_passes_list(self):
        """
        Тестирование эндпоинта /status-passes/list
        Endpoint testing: /status-passes/list
        """
        url = self._BASE_TESTING_URL + "/status-passes/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_time_day_list(self):
        """
        Тестирование эндпоинта /pass-type-by-time-of-the-day/list
        Endpoint testing: /pass-type-by-time-of-the-day/list
        """
        url = self._BASE_TESTING_URL + "/pass-type-by-time-of-the-day/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_pass_time_list(self):
        """
        Тестирование эндпоинта /pass-type/list
        Endpoint testing: /pass-type/list
        """
        url = self._BASE_TESTING_URL + "/pass-type/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_app_status_list(self):
        """
        Тестирование эндпоинта /status/list
        Endpoint testing: /status/list
        """
        url = self._BASE_TESTING_URL + "/application/status/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_comp_list(self):
        """
        Тестирование эндпоинта /company/list
        Endpoint testing: /company/list
        """
        url = self._BASE_TESTING_URL + "/company/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_transp_list(self):
        """
        Тестирование эндпоинта /transport_owner_by_vrc/list
        Endpoint testing: /transport_owner_by_vrc/list
        """
        url = self._BASE_TESTING_URL + "/transport_owner_by_vrc/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_serv_list(self):
        """
        Тестирование эндпоинта /services/list
        Endpoint testing: /services/list
        """
        url = self._BASE_TESTING_URL + "/services/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_post_serv_list(self):
        """
        Тестирование эндпоинта /update
        Endpoint testing: /update
        """
        url = self._BASE_TESTING_URL + "/update"
        response: Response = requests.post(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_post_app_creat_upd(self):
        """
        Тестирование эндпоинта /application/create-or-update
        Endpoint testing: /application/create-or-update
        """
        url = self._BASE_TESTING_URL + "/application/create-or-update"
        response: Response = requests.post(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_post_creat_upd_company(self):
        """
        Тестирование эндпоинта /create-or-update/company
        Endpoint testing: /create-or-update/company
        """
        url = self._BASE_TESTING_URL + "/create-or-update/company"
        response: Response = requests.post(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )

    def test_unauth_access_post_creat_upd_trans_own(self):
        """
        Тестирование эндпоинта /create-or-update/transport_owner_by_vrc
        Endpoint testing: /create-or-update/transport_owner_by_vrc
        """
        url = (
            self._BASE_TESTING_URL + "/create-or-update/transport_owner_by_vrc"
        )
        response: Response = requests.post(url)
        self._check_authorisation(response)

        response_data = response.json()
        self._check_message_key(response)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"{self._ERR_UNAUTH_MSG} {response_data['message']}",
        )


if __name__ == "__main__":
    unittest.main()
