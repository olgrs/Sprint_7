BASE_URL = 'https://qa-scooter.education-services.ru/api/v1/'
COURIER_URL = 'courier'
ORDERS_URL = 'orders'
LOGIN_URL = 'courier/login'
DELETE_COURIER_URL = 'courier/'

ORDER_DATA = [
    {
        "firstName": "Иван",
        "lastName": "Иванов",
        "address": "ул. Ленина, 1",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2026-06-06",
        "comment": "Тестовый заказ",
        "color": ["BLACK"]
    },
    {
        "firstName": "Петр",
        "lastName": "Петров",
        "address": "ул. Пушкина, 2",
        "metroStation": 10,
        "phone": "+7 900 000 00 00",
        "rentTime": 3,
        "deliveryDate": "2026-07-07",
        "comment": "",
        "color": ["GREY"]
    },
    {
        "firstName": "Анна",
        "lastName": "Сидорова",
        "address": "ул. Цветочная, 5",
        "metroStation": 22,
        "phone": "+7 901 234 56 78",
        "rentTime": 1,
        "deliveryDate": "2026-08-08",
        "comment": "Два цвета",
        "color": ["BLACK", "GREY"]
    },
    {
        "firstName": "Олег",
        "lastName": "Олегов",
        "address": "ул. Лесная, 7",
        "metroStation": 15,
        "phone": "+7 902 345 67 89",
        "rentTime": 7,
        "deliveryDate": "2026-09-09",
        "comment": "Без цвета",
        "color": []
    }
]
LOGIN_DATA_MISSING_FIELD = [
    {"login": "", "password": "1234"},
    {"login": "ninja", "password": ""}
]
