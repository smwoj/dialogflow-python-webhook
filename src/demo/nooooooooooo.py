from _api_dispatcher import register_intent
from dialogflow_spec import make_response
from dialogflow_spec.widgets import GACard, GAButton


@register_intent('noooooooooooooooo')
def noooooooooooo_handler(_request_data):
    card = GACard(
        title=''''Vader's a bit upset!''',
        formatted_text="",
        image_url='http://www.bardfieldacademy.org/wp-content/uploads/2016/08/blue-button-for-web.jpg',
        image_hint="no good",
        buttons=[
            GAButton(
                title='PUSH ME',
                url='http://www.nooooooooooooooo.com/'
            )
        ]
    )
    return make_response('Nooooooooooooo!!!', card)
