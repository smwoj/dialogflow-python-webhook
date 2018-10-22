from _api_dispatcher import register_intent
from pprint import pformat


@register_intent('hello_api_intent')
def hello_api_intent(intent, **params):
    return f"This should be displayed. " \
           f"Request for intent {intent} received and correctly handled. " \
           f"Received params: " + pformat(params)
