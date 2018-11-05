import os

HOST = '0.0.0.0'
PORT = 8080
APP_NAME = 'DialogFlow Webhook Service'
API_ENDPOINTS = {'demo'}
ROOT = os.path.dirname(os.path.abspath(__file__))


def get_api_endpoint(*, api_version):
    assert api_version in API_ENDPOINTS
    return "http://" + HOST + ":" + str(PORT) + f"/api/{api_version}"
