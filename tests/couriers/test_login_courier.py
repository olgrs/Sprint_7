import allure
import pytest
from data import LOGIN_DATA_MISSING_FIELD


class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_success(self, courier_methods, courier):
        response = courier_methods.login_courier(courier['login'], courier['password'])
        assert response.status_code == 200 and 'id' in response.json()

    @allure.title("Ошибка при неверном логине")
    def test_login_invalid_login(self, courier_methods, courier):
        response = courier_methods.login_courier('invalid_login', courier['password'])
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.json()['message']

    @allure.title("Ошибка при неверном пароле")
    def test_login_invalid_password(self, courier_methods, courier):
        response = courier_methods.login_courier(courier['login'], 'invalid_password')
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.json()['message']

    @allure.title("Ошибка при отсутствии обязательного поля")
    @pytest.mark.parametrize('payload', LOGIN_DATA_MISSING_FIELD)
    def test_login_missing_required_field(self, courier_methods, payload):
        response = courier_methods.login_courier(payload['login'], payload['password'])
        assert response.status_code == 400 and 'Недостаточно данных для входа' in response.json()['message']

    @allure.title("Ошибка при авторизации несуществующего пользователя")
    def test_login_nonexistent(self, courier_methods):
        response = courier_methods.login_courier('nonexistent', 'password')
        assert response.status_code == 404 and 'Учетная запись не найдена' in response.json()['message']
