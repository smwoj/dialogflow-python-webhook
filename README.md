# dialogflow-python-webhook

Python implementation of a simple Flask-based webhook for dialogflow agent.

It's designed with experimentation in mind and quite a bare-bones solution, 
but allows you to make a simple, but highly extensible voice assistant reachable from your Android device in 30 minutes.

# How does it work?
Custom Google Action can be implemented in Dialogflow, which is an out-of-the-box Google's NLU sollution.

Simply speaking, when you speak to your custom Google Action, Google assistant takes care of speech recognition 
and forwards the utterance to the DialogFlow agent. 
DialogFlow performs NLU and attempts to match an intent defined for a given agent (agents are in 1:1 relation to Google Assistant).

Intents are defined within the DialogFlow agent. Intent definition requires training utterances (obviously), 
slots definition and fulfillment method, which is called when a user utters a sentence matching this intent.

One of the fulfillment possibilities is providing your own webhook. Dialogflow will send a POST request to a webservice you provide.
This request will contain all the data related to the user's utterance (full utterance, matched slots, conversation id and others).
In return, Dialogflow will expect a response with text that should be read to the user by Google Assistant TTS.

That's where this project comes in.

# What's in this project

A ready-to-go webserver containg an examplary definition of a dead-simple intent fullfillment implementation.

There also a small testing framework that mocks DialogFlow requests to allow testing locally.

You can deploy it with Google AppEngine, Heroku or any other way you like, 
but if you're doing this for fun, probably the simplest solution is using ngrok (ADD LINK) and running the webhook locally.

