import os, glob, importlib
import _constants as const

_INTENTS = {}


def register_intent(intent_name):  # add option - interface=choice['basic', 'full']

    def registerer(intent_handler):
        _INTENTS[intent_name] = intent_handler
        return intent_handler

    return registerer


def _execute_submodules(api_endpoint):
    api_handlers_pattern = os.path.join(const.ROOT, api_endpoint, '*')

    for filepath in (fp for fp in glob.glob(api_handlers_pattern)
                     if not fp.endswith('__init__.py')):
        module_name = os.path.split(filepath)[1].strip('.py')
        importlib.import_module(api_endpoint + '.' + module_name)


def import_intent_handlers(api_endpoint):
    assert api_endpoint in const.API_ENDPOINTS, f"Unrecognized endpoint: {api_endpoint}. Maybe add to constants?"

    _execute_submodules(api_endpoint)
    return _INTENTS
