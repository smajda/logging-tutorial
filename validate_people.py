import argparse
import logging
import sys

from os.path import abspath, dirname, join

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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path of file to import')
    args = parser.parse_args()
    validate_csv(args.filepath)
