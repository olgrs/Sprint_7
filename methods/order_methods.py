import allure
import requests
from data import BASE_URL, ORDERS_URL


class OrderMethods:

    def __init__(self):
        self.url = f'{BASE_URL}{ORDERS_URL}'

    @allure.step("Создание заказа")
    def create_order(self, order_data):
        return requests.post(self.url, json=order_data)

    @allure.step("Получить список заказов")
    def get_orders_list(self, params=None):
        return requests.get(self.url, params=params)
