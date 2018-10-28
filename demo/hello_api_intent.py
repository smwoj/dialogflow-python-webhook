from _api_dispatcher import register_intent
from pprint import pformat


@register_intent('hello_api_intent')
def hello_api_intent(intent, **params):
    return f"This should be displayed. " \
           f"Request for intent {intent} received and correctly handled. " \
           f"Received params: " + pformat(params)


@register_intent('joke-teller')
def joke_teller(intent, **params):
    if params['joke-type'] == 'dirty':
        return 'As I suspected, someone has been adding soil to my garden. The plot thickens.'
    elif params['joke-type'] == 'silly':
        return "Why aren’t koalas actual bears? The don’t meet the koalafications."
    else:
        return f'''Sorry, but I don't know any jokes of this type - {params["joke-type"]}.'''
