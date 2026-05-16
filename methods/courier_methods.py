import allure
import random
import requests
import string

from data import BASE_URL, COURIER_URL


class CourierMethods:
    TIMEOUT = 10  

    def __init__(self):
        self.base_url = f'{BASE_URL}{COURIER_URL}'

    @staticmethod
    def generate_courier_data():
        def gen(length=10):
            return ''.join(random.choices(string.ascii_lowercase, k=length))
        return {
            "login": gen(),
            "password": gen(),
            "firstName": gen()
        }

    @allure.step("Создать курьера")
    def create_courier(self, params=None):
        if params is None:
            params = self.generate_courier_data()
        response = requests.post(self.base_url, json=params, timeout=self.TIMEOUT)
        return response

    @allure.step("Логин курьера")
    def login_courier(self, login, password):
        response = requests.post(
            f'{self.base_url}/login',
            json={"login": login, "password": password},
            timeout=self.TIMEOUT
        )
        return response

    @allure.step("Авторизовать курьера")
    def authorize_courier(self, login, password):
        return self.login_courier(login, password)

    @allure.step("Удалить курьера")
    def delete_courier(self, courier_id):
        response = requests.delete(
            f'{self.base_url}/{courier_id}',
            timeout=self.TIMEOUT
        )
        return response
    
    @allure.step("Логин курьера (JSON)")
    def login_courier_raw(self, payload):
        response = requests.post(
            f'{self.base_url}/login',
            json=payload,
            timeout=self.TIMEOUT
        )
        return response
