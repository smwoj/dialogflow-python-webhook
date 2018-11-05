import json


def make_request(nlu_utterance, intent, parameters=None):
    request = {
        "responseId": "6e008853-aefd-4d18-b7c2-0f945cd91bb3",
        "queryResult": {
            "queryText": nlu_utterance,
            "parameters": parameters or {},
            "allRequiredParamsPresent": True,
            "intent": {
                "name": "projects/hackathon-app-220820/agent/intents/5a6f8efc-90b4-4f8a-bb84-a17b7aad2c55",
                "displayName": intent
            },
            "intentDetectionConfidence": 1,
            "languageCode": "en"
        },
        "originalDetectIntentRequest": {
            "payload": {}
        },
        "session": "projects/hackathon-app-220820/agent/sessions/6a5cac36-1994-f60d-cc60-e7721112ffa8"
    }
    return json.dumps(request)


def make_response(tts_msg, *ga_objects):
    response = {
        "fulfillmentText": '',
        "fulfillmentMessages": [],
        "source": "hackathon-webhook.com",
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": tts_msg,
                            }
                        },
                        *ga_objects
                    ]
                }
            },
        },
    }
    return json.dumps(response)
