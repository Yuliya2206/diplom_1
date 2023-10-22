#Дементьева Юлия 9 когорта Дипломный проект
import configuration
import requests
import data

# Создание заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS,
                         json=body,
                         headers=data.header_content)

# Получение заказа по номеру трекера
def get_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.REQUEST_ORDER,
                        track=track_number)

# Автотест
def create_order():
    current_body = data.order_body.copy()
    track_num = post_new_order(current_body)

    return str(track_num.json()["track"])

def positive_assert():
    track_num = create_order()
    current_param = data.params_get.copy()
    current_param["t"] = track_num
    response = get_order(current_param)
    assert response.status_code == 200
def test_order():
    positive_assert()





