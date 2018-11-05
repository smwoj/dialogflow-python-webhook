from _api_dispatcher import register_intent
from dialogflow_spec import make_response


@register_intent('joke-teller')
def joke_teller(request_data):
    params = request_data['queryResult']['parameters']

    joke_type_to_response = {
        'dirty': 'As I suspected, someone has been adding soil to my garden. The plot thickens.',
        'silly': "Why aren’t koalas actual bears? The don’t meet the koalafications.",
        'dad': "What do you call a Mexican who has lost his car? Carlos."
    }
    message = joke_type_to_response.get(
        params['joke-type'],
        f'''Sorry, but I don't know any jokes of this type - {params["joke-type"]}.''')

    return make_response(tts_msg=message)
