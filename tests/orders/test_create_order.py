import allure
import pytest
from data import ORDER_DATA


class TestCreateOrder:

    @allure.title("Успешное создание заказа: проверка наличия track в ответе")
    @pytest.mark.parametrize("order_data", ORDER_DATA)
    def test_create_order_success(self, order_methods, order_data):
        response = order_methods.create_order(order_data)
        assert response.status_code == 201 and 'track' in response.json(), (
            f"Ожидался статус 201 и наличие 'track' в ответе, "
            f"но получен статус {response.status_code} и тело {response.text}"
        )
