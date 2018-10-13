import io, sys, argparse, pprint, json, requests
import _constants as const

"""
Convenient POST-er for local development.
"""

ENDPOINT = const.get_api_endpoint(api_version='demo')


def parse_cl_args(args):
    # TODO: allow choosing api endpoint

    parser = argparse.ArgumentParser(description='Test the webhook running on local server.')
    parser.add_argument('-u', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    return parser.parse_args(args)


if __name__ == '__main__':
    args = parse_cl_args(sys.argv[1:])

    from dialogflow_spec import _bigass_json
    print(
        # json.loads(
            requests.post(ENDPOINT, json=_bigass_json).content.decode()
        # )
    )
