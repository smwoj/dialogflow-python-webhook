import _constants as const
from _app import app

"""
TODO: pycurl test for local development
'demo' api endpoint
"""

if "__main__" == __name__:
    app.run(debug=True, host=const.HOST, port=const.PORT)
