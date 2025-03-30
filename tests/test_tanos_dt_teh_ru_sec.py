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

    # Выводим в случае ответа, отличного от Unauthorized
    # Show if the response is not Unauthorized
    ERR_UNAUTH_MSG = 'Ожидается "Unauthorized" получено'

    def _check_authorisation(self, response: Response) -> None:
        """Проверяет на корректность ответа
        Ожидаю ошибку 401
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
        Проверяю ключ "massage"
        """

        self.assertIn(
            "message",
            response_data,
            'Ключ "message" не найден в ответе от сервера',
        )

    def test_unauth_access_list(self):
        """
        Тестирование эндпоинта /list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/list"
        response: Response = requests.get(url)
        self._check_authorisation(response)
        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response.json()["message"],
            "Unauthorized",
            f" {response_data['message']}",
        )

    def test_unauth_access_app_list(self):
        """
        Тестирование эндпоинта /application/list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/application/list"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self._check_message_key(response_data)
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_app_export(self):
        """
        Тестирование эндпоинта /application/export
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/application/export"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_allowed_zona_passes_list(self):
        """
        Тестирование эндпоинта /allowed-zona-passes/list
        """
        url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/allowed-zona-passes/list"
        )
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )

        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_status_passes_list(self):
        """
        Тестирование эндпоинта /status-passes/list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/status-passes/list"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_time_day_list(self):
        """Тестирование эндпоинта /pass-type-by-time-of-the-day/list"""
        url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/"
            "pass-type-by-time-of-the-day/list"
        )
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_pass_time_list(self):
        """
        Тестирование эндпоинта /pass-type/list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/pass-type/list"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_app_status_list(self):
        """
        Тестирование эндпоинта /status/list
        """
        url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/application/status/list"
        )
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_comp_list(self):
        """
        Тестирование эндпоинта /company/list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/company/list"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_transp_list(self):
        """
        Тестирование эндпоинта /transport_owner_by_vrc/list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/transport_owner_by_vrc/list"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_serv_list(self):
        """
        Тестирование эндпоинта /services/list
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/services/list"
        response: Response = requests.get(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_post_serv_list(self):
        """
        Тестирование эндпоинта /update
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/update"
        response: Response = requests.post(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_post_app_creat_upd(self):
        """
        Тестирование эндпоинта application/create-or-update
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/application/create-or-update"
        response: Response = requests.post(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_post_creat_upd_company(self):
        """
        Тестирование эндпоинта /create-or-update/company
        """
        url = (
            "https://tanos-cp.dt-teh.ru/api/passes/v1/create-or-update/company"
        )
        response: Response = requests.post(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )

    def test_unauth_access_post_creat_upd_trans_own(self):
        """
        Тестирование эндпоинта /create-or-update/transport_owner_by_vrc
        """
        url = "https://tanos-cp.dt-teh.ru/api/passes/v1/create-or-update/transport_owner_by_vrc"
        response: Response = requests.post(url)

        err_msg = (
            f"Ошибка авторизации или неверные учетные данные: "
            f"{response.status_code}"
        )
        self.assertEqual(
            response.status_code,
            401,
            err_msg,
        )

        response_data = response.json()
        self.assertIn(
            "message",
            response_data,
            "Ключ message не найден в ответе от сервера",
        )
        self.assertEqual(
            response_data["message"],
            "Unauthorized",
            f"ERR_UNAUTH_MSG {response_data['message']}",
        )


if __name__ == "__main__":
    unittest.main()
