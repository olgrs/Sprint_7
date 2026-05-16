import pytest
import random
import string
from methods.courier_methods import CourierMethods
from methods.order_methods import OrderMethods


@pytest.fixture
def courier_methods():
    return CourierMethods()

@pytest.fixture
def order_methods():
    return OrderMethods()

def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

@pytest.fixture
def new_courier(courier_methods):
    """Создаёт курьера, возвращает (response, data, courier_id). Удаляет после теста."""
    data = {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }
    response = courier_methods.create_courier(data)
    login_resp = courier_methods.login_courier(data['login'], data['password'])
    courier_id = login_resp.json()['id']
    yield response, data, courier_id
    courier_methods.delete_courier(courier_id)

@pytest.fixture()
def authorize_courier(courier):
    response = courier[2].authorize_courier(courier[1])
    return response.json()['id']

@pytest.fixture
def courier(new_courier):
    """Возвращает словарь с login, password, id."""
    _, data, courier_id = new_courier
    return {
        'login': data['login'],
        'password': data['password'],
        'id': courier_id
    }

@pytest.fixture
def authorize_courier(courier_methods, courier):
    response = courier_methods.authorize_courier(courier['login'], courier['password'])
    assert response.status_code == 200
    return response.json()['id']
