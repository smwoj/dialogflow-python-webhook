# data & utils specific for DialogFlow webhook protocol

# parse(request: DialogflowPOSTRequest) -> NLUData (utterance + slots_dict)

# format_response(utterance: str) -> DialogFlowWebhookResponse

from flask import jsonify


# INPUT REQUEST
def _parse_request():
    return {'country': 'Poland'}


_bigass_json = """
{
  "responseId": "6e008853-aefd-4d18-b7c2-0f945cd91bb3",
  "queryResult": {
    "queryText": "tell me a silly joke",
    "parameters": {
      "joke-type": "silly"
    },
    "allRequiredParamsPresent": true,
    "intent": {
      "name": "projects/hackathon-app-220820/agent/intents/5a6f8efc-90b4-4f8a-bb84-a17b7aad2c55",
      "displayName": "joke-teller"
    },
    "intentDetectionConfidence": 1,
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {
    "payload": {}
  },
  "session": "projects/hackathon-app-220820/agent/sessions/6a5cac36-1994-f60d-cc60-e7721112ffa8"
}
"""


def make_response(display_message, tts_message):
    response = {
        "fulfillmentText": display_message,
        "fulfillmentMessages": [],
        "source": "mywebhook.com",
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": tts_message,
                            }
                        }
                    ]
                }
            },
        },
    }
    return jsonify(response)
