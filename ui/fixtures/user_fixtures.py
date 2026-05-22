from typing import Iterator

import httpx
import pytest
from ui.test_data.factories import UserFactory, UserData


@pytest.fixture
def api_client() -> Iterator[httpx.Client]:
    with httpx.Client() as client:
        yield client


@pytest.fixture
def user(api_client) -> UserData:
    user_info = UserFactory.create()

    response = api_client.post(
        "https://automationexercise.com/api/createAccount",
        data={
            "name": user_info.name,
            "email": user_info.email,
            "password": user_info.password,
            "title": user_info.title,
            "birth_date": user_info.day,
            "birth_month": user_info.month,
            "birth_year": user_info.year,
            "firstname": user_info.first_name,
            "lastname": user_info.last_name,
            "company": user_info.company,
            "address1": user_info.address,
            "address2": user_info.address2,
            "country": user_info.country,
            "zipcode": user_info.zipcode,
            "state": user_info.state,
            "city": user_info.city,
            "mobile_number": user_info.mobile_number,
        }
    )

    user_data = response.json()
    if user_data.get("responseCode") != 201:
        raise ValueError(f"Failed to create user: {user_data}")

    return user_info


@pytest.fixture
def user_with_cleanup(user: UserData, api_client: httpx.Client):
        yield user

        response_to_delete = api_client.request(
            method="DELETE",
            url="https://automationexercise.com/api/deleteAccount",
            data={
                "email": user.email,
                "password": user.password
            }
        )

        delete_data = response_to_delete.json()
        if delete_data.get("responseCode") != 200:
            raise ValueError(f"Failed to delete user: {delete_data}")


@pytest.fixture
def account_user_info() -> UserData:
    return UserFactory.create()