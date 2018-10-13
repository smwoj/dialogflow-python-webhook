from flask import Flask, jsonify
import _constants as const

app = Flask(const.APP_NAME)


@app.route('/')
def index():
    return f"Hello world from {const.APP_NAME}"


@app.route('/api/demo')
def _handler():
    return jsonify({'response': f"DEMO API handler root sends it's regards."})


# def register_intent(intent, endpoint):
#   assert endpoint in const.API_ENDPOINTS
#     def dec():
#         return fun
#     return dec