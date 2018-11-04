# dialogflow-python-webhook

Python implementation of a simple Flask-based webhook for dialogflow agent.

It's designed with experimentation in mind and quite a bare-bones solution, 
but allows you to make a simple, but highly extensible voice assistant reachable from your Android device in 30 minutes.

# How does it work?
Custom Google Action can be implemented in Dialogflow, which is an out-of-the-box Google's NLU solution.

Simply speaking, when you speak to your custom Google Action, Google assistant takes care of speech recognition 
and forwards the utterance to the DialogFlow agent.
DialogFlow performs NLU and attempts to match an intent defined for a given agent (agents are in 1:1 relation to Google Assistant).

Intents are defined within the DialogFlow agent. Intent definition requires training utterances (obviously), 
slots definition and fulfillment method, which is called when a user utters a sentence matching this intent.

One of the fulfillment possibilities is providing your own webhook. Dialogflow will send a POST request to a webservice you provide.
This request will contain all the data related to the user's utterance (full utterance, matched slots, conversation id and others).
In return, Dialogflow expects a response with text that should be read to the user by Google Assistant TTS.

That's where this project comes in.

# What's in this project

A ready-to-go webservice containing an exemplary definition 
of a dead-simple intent fulfillment implementation.

There also a small script mocking DialogFlow requests to allow local testing.

You can deploy it with Google AppEngine, Heroku or any other way you like, 
but if you're doing this for fun, probably the simplest solution is using 
[ngrok](https://ngrok.com/) and running the service locally.

# How to make my own Google Assistant Action with this repo?
1. Create a virtual environment from src/requirements.txt

2. Create a GCloud account and enable billing.
There's a generous trial period, so even though you have to register using your credit card,
you won't be charged unless you agree to when the trial ends or you exhaust the limits.

3. Create a new project in [actions console](https://console.actions.google.com/).
Skip the choice of the action template (assuming you still want to use this project).

4. You'll be moved to your new action's dashboard. You can set up a an action invocation here,
test the action (later on) and set up the action implementation.

    Move to Actions - Add your first action - (Custom Intent) Build.

    (You will land on the new Dialogflow agent creation page.)

5. This is the dashboard, where you have to define intents
you want to implement and entities for matching intent parameters (slots).
In the simplest form:
    - define an intent name in 'Intents'.
    - add some training phrases and annotate parameters (slots).
    - optionally, add custom entities/parameters. There are a few predefined entities,
    such as 'sys.given-name' or 'sys.country-code', but you can define you own parameter in the 'Entities' tab.
    The exemplary intent implementation ('joke-teller' from 'demo' endpoint), for example, uses a mandatory 'joke-type' parameter.

6. Create a new directory (src/$your-endpoint) to contain the implementations of your intents ('src/demo' is an example).
The intent implementation should accept a parsed request json and return a response to the user.
(a simple string, the DialogFlow response format is already taken care of).
The demo implementations should be clear enough.

6. Run the webservice with 'python main $your_endpoint'.

7. (optional) Adjust the CMD in the Dockerfile to use $your-endpoint instead of 'demo'
if you want to deploy this app somewhere (with ngrok-like tunneling being the alternative).

8. When you move back to [actions console](https://console.actions.google.com/) of your project, choose 'Simulator'.
It will allow you to test your Action. If you have an Android device, you can test the Action on it,
as long as you're logged in with the same account. You can also grant this privilege to other Google accounts.
