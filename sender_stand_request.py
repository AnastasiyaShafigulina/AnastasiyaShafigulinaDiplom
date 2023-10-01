import configuration
import requests
import data


# функция cоздания заказ
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=order_body)


# функция сохранения номера заказа
def get_track():
    order_track = post_new_order(data.order_body)
    return order_track.json()["track"]


# функция получения заказа по треку
def get_order_by_track(order_track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_TRACK_PATH + str(order_track))
