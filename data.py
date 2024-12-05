# заголовки для HTTP-запроса, указывающие на то, что тело запроса будет в формате JSON
headers = {
    "Content-Type": "application/json"
}

# тело запроса POST создания заказа
body_order = {
    "firstName": "Артем",
    "lastName": "Кукушкин",
    "address": "Вешних вод, 14-155",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2024-12-06",
    "comment": "Позвоните за 10 мин",
    "color": [
        "BLACK"
    ]
}
