import json
from pprint import pprint, pformat
from flask import Flask, jsonify, request
import _constants as const

app = Flask(const.APP_NAME)


@app.route('/')
def index():
    return f"Hello, user, from {const.APP_NAME}!"


@app.route('/api/demo', methods=['GET'])
def _handler():
    return jsonify({'response': f"DEMO API handler root sends it's regards."})


def __hhhandler(intent, **params):
    return f"This should be displayed. Request for intent {intent} received and correctly handled. Received params: " + pformat(params)


@app.route('/api/demo', methods=['POST'])
def _post_handler():
    request_data = request.get_json()
    print(f"req_json type = {type(request_data)}\n {request_data}")

    if isinstance(request_data, str):
        request_data = json.loads(request_data)

    pprint(request_data)
    intent = request_data['queryResult']['intent']['name']
    params = request_data['queryResult']['parameters']

    msg = __hhhandler(intent, **params)

    from dialogflow_spec import make_response
    return make_response(
        display_message=msg,
        tts_message="And this should be read.",
    )


# def register_intent(intent, endpoint):
#   assert endpoint in const.API_ENDPOINTS
#     def dec():
#         return fun
#     return dec
