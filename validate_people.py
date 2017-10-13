import argparse

from people.tasks import validate_csv


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path of file to import')
    args = parser.parse_args()
    validate_csv(args.filepath)
