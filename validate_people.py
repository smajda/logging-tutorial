import argparse
import logging
import json
import os
import sys

from os.path import abspath, dirname, join

import requests

from people.tasks import validate_csv

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# add a simple formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# let's add a custom StreamHandler
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(logging.ERROR)
logger.addHandler(stream_handler)

# and a FileHandler
file_handler = logging.FileHandler(filename=join(abspath(dirname(__name__)), 'validate_people.log'))
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# how about a Slack handler?
class SlackHandler(logging.Handler):
    def __init__(self, webhook_url, *args, **kwargs):
        self.webhook_url = webhook_url
        super().__init__(*args, **kwargs)

    def emit(self, record):
        text = self.format(record)
        data = {
            'text': text,
            # channel, username, icon, attachments, etc
        }
        requests.post(self.webhook_url, json.dumps(data))


webhook_url = os.environ.get("SLACK_WEBHOOK_URL")
if webhook_url:
    slack_handler = SlackHandler(webhook_url=webhook_url)
    slack_handler.setLevel(logging.ERROR)
    slack_handler.setFormatter(formatter)
    logger.addHandler(slack_handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path of file to import')
    parser.add_argument("--verbose", "-v", action="count", default=0, help="increase verbosity")
    args = parser.parse_args()

    loglevel = logging.ERROR - args.verbose * 10
    stream_handler.setLevel(loglevel)

    validate_csv(args.filepath)
