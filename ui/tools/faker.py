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

    def password(self) -> str:
        return self.faker.password()

    def name(self) -> str:
        return self.faker.name()

    def date_of_birth(self) -> dict:
        dob = self.faker.date_of_birth(minimum_age=18, maximum_age=60)
        return {
            "day": str(dob.day),
            "month": dob.strftime("%B"),
            "year": str(dob.year)
        }

    def title(self) -> str:
        return random.choice(["mr", "mrs"])

    def first_name(self) -> str:
        return self.faker.first_name()

    def last_name(self) -> str:
        return self.faker.last_name()

    def company(self) -> str:
        return self.faker.company()

    def address(self) -> str:
        return self.faker.street_address()

    def address2(self) -> str:
        return self.faker.street_address()

    def country(self) -> str:
        return random.choice(self.COUNTRIES)

    def state(self) -> str:
        return self.faker.state()

    def city(self) -> str:
        return self.faker.city()

    def zipcode(self) -> str:
        return self.faker.zipcode()

    def mobile_number(self) -> str:
        return self.faker.phone_number()

    def subject(self) -> str:
        return self.faker.sentence(nb_words=7)

    def paragraph(self, sentences=20) -> str:
        return self.faker.paragraph(nb_sentences=sentences)

    def quantity(self) -> int:
        return random.randint(1,100)

    def credit_card_number(self) -> str:
        return self.faker.credit_card_number()

    def credit_card_security_code(self) -> str:
        return self.faker.credit_card_security_code()

    def credit_card_expire_month(self) -> str:
        return self.faker.credit_card_expire(date_format="%m")

    def credit_card_expire_year(self) -> str:
        return self.faker.credit_card_expire(date_format="%Y")

fake = Fake(faker=Faker())

