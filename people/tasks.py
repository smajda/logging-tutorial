import csv
import logging

from .schema import Person

logger = logging.getLogger(__name__)


def validate_csv(path):
    schema = Person()

    with open(path, 'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            errors = schema.validate(row)

            if 'birthdate' in errors:
                logger.error(f"{i} birthdate: {', '.join(errors['birthdate'])}")

            if 'name' in errors:
                logger.error(f"{i} name: {', '.join(errors['name'])}")

            if not errors:
                logger.debug(f"{i} success: {row['name']} is valid!")
