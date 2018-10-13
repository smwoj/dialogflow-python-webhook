HOST = 'localhost'
PORT = 8080
ENCODING = 'iso-8859-1'
APP_NAME = 'DialogFlow Webhook Service'
API_ENDPOINTS = {'demo'}


def get_api_endpoint(*, api_version):
    assert api_version in API_ENDPOINTS
    return "http://" + HOST + ":" + str(PORT) + f"/api/{api_version}"
