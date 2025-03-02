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
        responce_data = responce.json()
        self.assertIn("message",
                      responce_data,
                      "Ключ message не найден в ответе от сервера")
        
        self.assertEqual(responce_data["message"], 
                         "Unauthorized", 
                          f"Ожидается  \"Unauthorized\" получено {responce_data['message']}")


if __name__ == "__main__":
    unittest.main()