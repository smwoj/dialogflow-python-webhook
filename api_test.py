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


"""
 2003  sudo docker build -t df-app:minimal
 2004  sudo docker build -t df-app:minimal .
 2005  sudo docker run 
 2006  sudo docker run -p 8080 -d -n df-app  df-app:minimal
 2007  sudo docker run -p 8080 -d --name df-app  df-app:minimal
 2008  sudo docker container ls -a
 2009  sudo docker stop df-app
 2010  sudo docker rm df-app
 2011  sudo docker rm vibrant-liskov
 2012  sudo docker container ls -a
 2013  sudo docker rm vibrant_liskov
 2014  sudo docker container ls -a
 2015  clear
 2016  sudo docker run -p 8080:8080 -d --name df-app  df-app:minimal
 2017  gcloud
 2018  gcloud project
 2019  gcloud projects
 2020  gcloud projects --help
 2021  gcloud projects set
 2022  gcloud project
 2023  gcloud set project
 2024  gcloud project
 2025  gcloud auth configure-docker
 2026  gcloud components update
 2027  gcloud config set project hackathon-webhooks
 2028  history

"""