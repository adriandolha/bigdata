from test.cars import *


def test_car_model_default():
    assert Car().model == "BMW"


def test_car_model_provided():
    assert Car("Nissan").model == "Nissan"
