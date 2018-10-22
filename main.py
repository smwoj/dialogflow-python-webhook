import os, sys, json, pprint
from flask import Flask, jsonify, request

import _constants as const
from _api_dispatcher import import_intent_handlers

"""
Usage: 
python main.py /api/$API_ENDPOINT
"""


def start(api_endpoint):
    app = Flask(const.APP_NAME)
    intent_handlers = import_intent_handlers(api_endpoint)

    @app.route('/')
    def index():
        return f"Hello, user, from {const.APP_NAME}!"

    @app.route(f'/api/{api_endpoint}', methods=['GET'])
    def _welcome_page_handler():
        return jsonify({'response': f"Successfully accessed GET from endpoint {api_endpoint}"})

    @app.route(f'/api/{api_endpoint}', methods=['POST'])
    def _api_dispatcher():
        request_data = request.get_json()
        request_data = json.loads(request_data)

        pprint.pprint(request_data)

        intent = request_data['queryResult']['intent']['displayName']
        params = request_data['queryResult']['parameters']

        msg = intent_handlers[intent](intent, **params)

        from dialogflow_spec import make_response
        return make_response(
            display_message=msg,
            tts_message="And this should be read.",
        )

    app.run(debug=True, host=const.HOST, port=const.PORT)


if "__main__" == __name__:
    assert os.getcwd() == const.ROOT, f"The server must be run from repo root dir: {const.ROOT}"

    start(api_endpoint=sys.argv[1])
