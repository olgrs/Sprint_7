import allure


class TestGetOrdersList:

    @allure.title("Получение списка заказов")
    def test_get_orders_list_success(self, order_methods):
        response = order_methods.get_orders_list()
        assert response.status_code == 200 and 'orders' in response.json(), (
            f"Ожидался статус 200 и наличие 'orders' в ответе, "
            f"но получен статус {response.status_code} и тело {response.text}"
        )
