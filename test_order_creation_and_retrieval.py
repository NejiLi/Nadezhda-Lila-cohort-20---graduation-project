
import sender_stand_request
import data

# Надежда Лила, 20-я когорта - дипломный проект
# Функция для проверки создания заказа и получения информации о нем по треку.

def test_order_creation_and_retrieval():
    # Создание нового заказа
    order_response = sender_stand_request.post_new_order(data.order_body)

    # Проверка статуса ответа и наличия трека заказа
    assert order_response.status_code == 201
    assert order_response.json().get('track') is not None

    # Сохранение трека заказа
    track = order_response.json().get('track')

    # Получение информации о заказе по треку
    info_response = sender_stand_request.get_info_order_track(track)

    # Проверка статуса ответа и наличия данных о заказе
    assert info_response.status_code == 200
    assert info_response.json() is not None
