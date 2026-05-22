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
        return random.choice(["mr", "mrs"])

    def first_name(self):
        return self.faker.first_name()

    def last_name(self):
        return self.faker.last_name()

    def company(self):
        return self.faker.company()

    def address(self):
        return self.faker.street_address()

    def address2(self):
        return self.faker.street_address()

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

    def paragraph(self, sentences=20):
        return self.faker.paragraph(nb_sentences=sentences)

    def quantity(self):
        return random.randint(1,100)

    def credit_card_number(self):
        return self.faker.credit_card_number()

    def credit_card_security_code(self):
        return self.faker.credit_card_security_code()

    def credit_card_expire_month(self):
        return self.faker.credit_card_expire(date_format="%m")

    def credit_card_expire_year(self):
        return self.faker.credit_card_expire(date_format="%Y")

fake = Fake(faker=Faker())

