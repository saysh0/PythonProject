import pytest
import requests

class BookingService:
    def __init__(self, base_url):
        self.base_url = base_url

    def create_booking(self, payload):
        return requests.post(f"{self.base_url}/booking", json=payload)

    def partial_update_booking(self, booking_id, payload, token):
        headers = {"Cookie": f"token={token}", "Content-Type": "application/json", "Accept": "application/json"}
        return requests.patch(f"{self.base_url}/booking/{booking_id}", json=payload, headers=headers)

    def get_auth_token(self, username, password):
        payload = {"username": username, "password": password}
        response = requests.post(f"{self.base_url}/auth", json=payload)
        return response.json().get("token")


@pytest.fixture
def api():
    return BookingService("https://restful-booker.herokuapp.com")


@pytest.fixture
def auth_token(api):
    return api.get_auth_token("admin", "password123")


def test_create_booking(api):
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"}
    }
    response = api.create_booking(payload)
    assert response.status_code == 200
    assert response.json()["booking"]["firstname"] == "Jim"


def test_partial_update_booking(api, auth_token):
    initial_payload = {"firstname": "Test", "lastname": "User", "totalprice": 100, "depositpaid": True, "bookingdates": {"checkin": "2026-01-01", "checkout": "2026-01-05"}}
    booking_id = api.create_booking(initial_payload).json()["bookingid"]
    update_data = {"firstname": "UpdatedName"}
    response = api.partial_update_booking(booking_id, update_data, auth_token)
    assert response.status_code == 200
    assert response.json()["firstname"] == "UpdatedName"


def test_negative_update(api):
    update_data = {"firstname": "Fail"}
    response = api.partial_update_booking(999999, update_data, token="invalid_token")
    assert response.status_code == 403