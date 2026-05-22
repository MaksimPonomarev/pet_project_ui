from dataclasses import dataclass
from ui.tools.faker import fake


@dataclass
class UserData:
    name: str
    password: str
    email: str
    first_name: str
    last_name: str
    company: str
    address: str
    address2: str
    country: str
    state: str
    city: str
    zipcode: str
    mobile_number: str
    day: int
    month: int
    year: int
    title: str

    def address_fields(self) -> dict:
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company": self.company,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zipcode": self.zipcode,
            "country": self.country,
        }


class UserFactory:
    @staticmethod
    def create(email: str = None, name: str = None) -> UserData:
        dob = fake.date_of_birth()
        return UserData(
            name=name or fake.name(),
            password=fake.password(),
            email=email or fake.email(),
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            company=fake.company(),
            address=fake.address(),
            address2=fake.address2(),
            country=fake.country(),
            state=fake.state(),
            city=fake.city(),
            zipcode=fake.zipcode(),
            mobile_number=fake.mobile_number(),
            day=dob["day"],
            month=dob["month"],
            year=dob["year"],
            title=fake.title()
        )
