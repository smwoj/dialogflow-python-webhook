import json, requests

import _constants as const
from dialogflow_spec import make_request

"""
Debug tool for local development.
"""

ENDPOINT = const.get_api_endpoint(api_version='demo')


if __name__ == '__main__':
    nlu_utterance = 'tell me a dad joke'
    intent = 'joke-teller'
    parameters = {'joke-type': 'dad'}

    req = make_request(nlu_utterance, intent, parameters)

    print(json.loads(
        requests.post(ENDPOINT, json=req).content.decode()
    ))
