import unittest
import requests

from requests import Response

class TestUnautorezedAccessPassesV1(unittest.TestCase):
    """Тестирование API пропуска на корректный ответ, когда пользователь
    не авторизован

    Args:
        unittest (_type_): _description_
    """
    def test_unauth_access_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        # print(responce.status_code)
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_app_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/application/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/application/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")

    def test_unauth_access_app_export(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/application/export
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/application/export"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")



    def test_unauth_access_allowed_zona_passes_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/allowed-zona-passes/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/allowed-zona-passes/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")
 
 
    def test_unauth_access_status_passes_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/status-passes/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/status-passes/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_time_day_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/pass-type-by-time-of-the-day/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/pass-type-by-time-of-the-day/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_pass_time_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/pass-type/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/pass-type/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_app_status_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/application/status/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/application/status/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_comp_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/company/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/company/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_transp_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/transport_owner_by_vrc/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/transport_owner_by_vrc/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


    def test_unauth_access_serv_list(self):
        """
            Тестирование эндпоинта https://tanos-cp.dt-teh.ru/api/passes/v1/services/list
        """
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/services/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


if __name__ == "__main__":
    unittest.main()