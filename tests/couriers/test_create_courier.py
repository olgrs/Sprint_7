import allure
import pytest
from methods.courier_methods import CourierMethods


class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self, new_courier):
        response, _, _ = new_courier
        assert response.status_code == 201 and response.json()['ok'] == True

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier(self, courier_methods, new_courier):
        _, data, _ = new_courier  
        response = courier_methods.create_courier(data)
        assert response.status_code == 409 and 'Этот логин уже используется' in response.json()['message']

    @allure.title("Создание курьера: отсутствует обязательное поле")
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_missing_field(self, courier_methods, missing_field):
        data = courier_methods.generate_courier_data()
        del data[missing_field]
        response = courier_methods.create_courier(data)
        assert response.status_code == 400 and 'Недостаточно данных для создания учетной записи' in response.json()['message']
