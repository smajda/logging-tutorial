import csv
import datetime

import faker

fake = faker.Faker()

HEADERS = ['name', 'birthdate']


DATE_RANGE = [datetime.date(1917, 1, 1), datetime.date(2017, 1, 1)]


def maybe_not(val):
    if fake.random.choice(range(0, 20)) == 0:
        return ''
    return val


def maybe_invalid(val):
    if fake.random.choice(range(0, 20)) == 0:
        return fake.text(15)
    return val


def save_fake_data():
    filename = f"data/people-{datetime.datetime.now().strftime('%Y%m%d%H%M')}.csv"
    with open(filename, 'wt') as f:
        writer = csv.writer(f)
        writer.writerow(HEADERS)
        for _ in range(0, 50):
            writer.writerow([
                maybe_not(fake.name()),
                maybe_invalid(
                    fake.date_between(DATE_RANGE[0], DATE_RANGE[1])
                ),
            ])


if __name__ == '__main__':
    save_fake_data()
