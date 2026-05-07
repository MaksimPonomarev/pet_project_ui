import uuid

from faker import Faker
import random

class Fake:
    COUNTRIES = [
        "India",
        "United States",
        "Canada",
        "Australia",
        "Israel",
        "New Zealand",
        "Singapore"
    ]

    def __init__(self, faker=None):
        self.faker = faker or Faker()

    def email(self, domain: str | None = None) -> str:
        return f"{uuid.uuid4()}{self.faker.email(domain=domain)}"

    def password(self):
        return self.faker.password()

    def name(self):
        return self.faker.name()

    def date_of_birth(self):
        dob = self.faker.date_of_birth(minimum_age=18, maximum_age=60)
        return {
            "day": str(dob.day),
            "month": dob.strftime("%B"),
            "year": str(dob.year)
        }

    def title(self):
        return random.randint(1,2)

    def first_name(self):
        return self.faker.first_name()

    def last_name(self):
        return self.faker.last_name()

    def company(self):
        return self.faker.company()

    def address(self):
        return self.faker.address()

    def address2(self):
        return self.faker.address()

    def country(self):
        return random.choice(self.COUNTRIES)

    def state(self):
        return self.faker.state()

    def city(self):
        return self.faker.city()

    def zipcode(self):
        return self.faker.zipcode()

    def mobile_number(self):
        return self.faker.phone_number()

    def subject(self):
        return self.faker.sentence(nb_words=7)

    def paragraph(self):
        return self.faker.paragraph(nb_sentences=20)

fake = Fake(faker=Faker())

