import csv

from .schema import Person


def validate_csv(path):
    schema = Person()

    with open(path, 'rt') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            errors = schema.validate(row)

            if 'birthdate' in errors:
                print(f'{i} birthdate: ', errors['birthdate'])

            if 'name' in errors:
                print(f"{i} name:", errors['name'])

            if not errors:
                print(f"{i} success: {row['name']} is valid")
