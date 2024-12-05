# Юлия Мокрова, 24-я когорта - Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request

def test_get_order_after_creating_success():
    current_body_order = data.body_order.copy()

    # Получение ответа на запрос создания нового заказа POST
    order_create_response = sender_stand_request.create_order(current_body_order)

    # Получение номера заказа из ответа (тип строка) и сохранение его в переменную track_order
    track_order = order_create_response.json()["track"]

    # Получение ответа на запрос GET заказа по его номеру
    get_order_response = sender_stand_request.get_order(track_order)

    # Проверка, что код ответа равен 200
    assert get_order_response.status_code == 200