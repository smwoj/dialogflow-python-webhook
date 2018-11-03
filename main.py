import os, sys, json, pprint
from flask import Flask, jsonify, request

import _constants as const
from _api_dispatcher import import_intent_handlers

"""
Usage: 
python main.py $API_ENDPOINT
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
        if isinstance(request_data, str):
            request_data = json.loads(request_data)

        intent = request_data['queryResult']['intent']['displayName']
        params = request_data['queryResult']['parameters']

        msg = intent_handlers[intent](intent, **params)


        from dialogflow_spec import make_response
        return make_response(
            display_message='',
            tts_message=msg,
        )

    app.run(debug=True, host=const.HOST, port=const.PORT
            # , ssl_context='adhoc'
            )


if "__main__" == __name__:
    assert os.getcwd() == const.ROOT, f"The server must be run from repo root dir: {const.ROOT}"

    start(api_endpoint=sys.argv[1])
"""
curl -H "Content-Type: application/json; charset=utf-8"  -H "Authorization: Bearer ya29.c.ElpJBjPI4X5IsxXp6ENtjAjcWCI4PhouvrKhhAAwrMsfDU8XqPQvBL062CGjEkkn8OUqoWrQmRIGoiwTOj2OyjIqjuQmd1eKS6Upo5RRwgFD1F3H2X-tbZ3eX8o"  -d "{\"queryInput\":{\"text\":{\"text\":\"tell me  a dirty joke\",\"languageCode\":\"en\"}},\"queryParams\":{\"timeZone\":\"Europe/Warsaw\"}}" "https://dialogflow.googleapis.com/v2/projects/hackathon-app-220820/agent/sessions/c937dbf8-d227-4eba-5dd9-36508dcd6cc5:detectIntent"
"""