import configuration
import requests
import data


# Cоздание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)


# Получить заказ по его номеру
def get_info_order_track(track):
    params_track = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.INFO_ORDER_PATH,
                        params=params_track)
