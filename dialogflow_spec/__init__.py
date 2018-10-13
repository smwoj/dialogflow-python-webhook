# data & utils specific for DialogFlow webhook protocol

# parse(request: DialogflowPOSTRequest) -> NLUData (utterance + slots_dict)

# format_response(utterance: str) -> DialogFlowWebhookResponse

from flask import jsonify

# INPUT REQUEST
def _parse_request():
    return {'country': 'Poland'}

_bigass_json = """
{
  "responseId": "13da0ef3-cb05-400d-a662-2f27ec00fb62",
  "queryResult": {
    "queryText": "make a sandwich for john",
    "parameters": {
      "given-name": "John"
    },
    "allRequiredParamsPresent": true,
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            ""
          ]
        }
      }
    ],
    "intent": {
      "name": "projects/custom-chatbot-85073/agent/intents/fd8a70ca-1e34-4201-acdb-37139c07e5a4",
      "displayName": "insult-person"
    },
    "intentDetectionConfidence": 1,
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {
    "payload": {}
  },
  "session": "projects/custom-chatbot-85073/agent/sessions/9f62edd8-6323-b183-0b7c-ef530b7ea349"
}"""


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


# RESPONSE EXAMPLE
# """
# {
#   "fulfillmentText": "This is a text response",
#   "fulfillmentMessages": [
#     {
#       "card": {
#         "title": "card title",
#         "subtitle": "card text",
#         "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
#         "buttons": [
#           {
#             "text": "button text",
#             "postback": "https://assistant.google.com/"
#           }
#         ]
#       }
#     }
#   ],
#   "source": "example.com",
#   "payload": {
#     "google": {
#       "expectUserResponse": true,
#       "richResponse": {
#         "items": [
#           {
#             "simpleResponse": {
#               "textToSpeech": "this is a simple response"
#             }
#           }
#         ]
#       }
#     },
#     "facebook": {
#       "text": "Hello, Facebook!"
#     },
#     "slack": {
#       "text": "This is a text response for Slack."
#     }
#   },
#   "outputContexts": [
#     {
#       "name": "projects/${PROJECT_ID}/agent/sessions/${SESSION_ID}/contexts/context name",
#       "lifespanCount": 5,
#       "parameters": {
#         "param": "param value"
#       }
#     }
#   ],
#   "followupEventInput": {
#     "name": "event name",
#     "languageCode": "en-US",
#     "parameters": {
#       "param": "param value"
#     }
#   }
# }
# """