# data & utils specific for DialogFlow webhook protocol

# parse(request: DialogflowPOSTRequest) -> NLUData (utterance + slots_dict)

# format_response(utterance: str) -> DialogFlowWebhookResponse

from flask import jsonify

# INPUT REQUEST
def _parse_request():
    return {'country': 'Poland'}

_bigass_json = """
{
  "responseId": "ea3d77e8-ae27-41a4-9e1d-174bd461b68c",
  "session": "projects/your-agents-project-id/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0",
  "queryResult": {
    "queryText": "user's original query to your agent",
    "parameters": {
      "country": "Poland"
    },
    "allRequiredParamsPresent": true,
    "fulfillmentText": "Text defined in Dialogflow's console for the intent that was matched",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Text defined in Dialogflow's console for the intent that was matched"
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/your-agents-project-id/agent/sessions/88d13aa8-2999-4f71-b233-39cbf3a824a0/contexts/generic",
        "lifespanCount": 5,
        "parameters": {
          "param": "param value"
        }
      }
    ],
    "intent": {
      "name": "projects/your-agents-project-id/agent/intents/29bcd7f8-f717-4261-a8fd-2d3e451b8af8",
      "displayName": "Matched Intent Name"
    },
    "intentDetectionConfidence": 1,
    "diagnosticInfo": {},
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {}
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