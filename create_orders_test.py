import data
import sender_stand_request


# основная функция

def test_get_order_by_track():
    data_order = sender_stand_request.get_order_by_track(sender_stand_request.get_track())
    assert data_order.status_code == 200

#Анастасия Шафигулина, 08-а когорта — Финальный проект. Инженер по тестированию плюс