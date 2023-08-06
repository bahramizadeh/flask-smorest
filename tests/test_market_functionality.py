import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        with app.app_context():
            yield client


# Functional test for '/markets/summaries' API
def test_get_markets_summaries_func_succeeded(client):
    # Providing access token
    api_url = "/login"
    response = client.post(api_url, json={"username": "maryam", "password": "123456dD"})

    token = response.json.get("access_token")

    endpoint = "/markets/summaries"
    response = client.get(endpoint, headers={"Authorization": f"Bearer {token}"})

    assert response.status_code == 200
    data = response.json

    assert isinstance(data, list)  # Assuming it returns a list of markets summaries


def test_get_markets_summaries_func_unsucceeded(client):

    endpoint = "/markets/summaries"
    response = client.get(endpoint)

    assert response.status_code == 401


# Functional test for '/markets/<string:marketSymbol>/summary' API
def test_get_market_summary_func_succeeded(client):
    # Providing access token
    api_url = "/login"
    response = client.post(api_url, json={"username": "maryam", "password": "123456dD"})

    token = response.json.get("access_token")
    market_symbol = "ltc-btc"

    endpoint = f"/markets/{market_symbol}/summary"
    response = client.get(endpoint, headers={"Authorization": f"Bearer {token}"})

    # Validate the response
    assert response.status_code == 200
    data = response.json
    assert isinstance(data, dict)  # Assuming it returns a single market summary


def test_get_market_summary_func_unsucceeded(client):

    market_symbol = "ltc-btc"

    endpoint = f"/markets/{market_symbol}/summary"
    response = client.get(endpoint)

    # Validate the response
    assert response.status_code == 401
