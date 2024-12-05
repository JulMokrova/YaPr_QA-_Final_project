import data

import configuration

import requests

def create_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.DOC_PATH_CREATE_ORDER,
                         json=body_order,
                         headers=data.headers)

def get_order(track_order):
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH_GET_ORDER+str(track_order))