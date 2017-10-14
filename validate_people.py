import argparse
import logging
import sys

from people.tasks import validate_csv

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# let's add a custom StreamHandler
stream_handler = logging.StreamHandler(stream=sys.stdout)
stream_handler.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path of file to import')
    args = parser.parse_args()
    validate_csv(args.filepath)
