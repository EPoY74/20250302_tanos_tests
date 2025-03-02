import unittest
import requests

from requests import Response

class TestUnautorezedAccess(unittest.TestCase):
    def test_unautorized_access_api_passes_v1_list(self):
        url: str ="https://tanos-cp.dt-teh.ru/api/passes/v1/list"
        responce: Response = requests.get(url)
        self.assertEqual(responce.status_code, 
                         401, 
                         f"Ошибка авторизации или неверные учетные данные: {responce.status_code}")


if __name__ == "__main__":
    unittest.main()