import pytest
from app import app
import json
from unittest.mock import patch

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

mock_teams_response = {
    "response": [
        {"team": {"id": 1, "name": "Team A"}},
        {"team": {"id": 2, "name": "Team B"}}
    ]
}

mock_matches_response = {
    "response": [
        {"fixture": {"id": 101}, "teams": {"home": {"name": "Team A"}, "away": {"name": "Team B"}}}
    ]
}

mock_league_info_response = {
    "response": [
        {"league": {"id": 39, "name": "La Liga"}}
    ]
}

def mock_requests_get_teams(*args, **kwargs):
    class MockResponse:
        def json(self_inner):
            return mock_teams_response
    return MockResponse()

def mock_requests_get_matches(*args, **kwargs):
    class MockResponse:
        def json(self_inner):
            return mock_matches_response
    return MockResponse()

def mock_requests_get_league_info(*args, **kwargs):
    class MockResponse:
        def json(self_inner):
            return mock_league_info_response
    return MockResponse()

@patch("requests.get", side_effect=mock_requests_get_teams)
def test_league_teams_success(mock_get, client):
    response = client.get("/league-teams?league=39")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "response" in data
    assert len(data["response"]) == 2

def test_league_teams_no_league(client):
    response = client.get("/league-teams")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data

@patch("requests.get", side_effect=mock_requests_get_matches)
def test_league_matches_success(mock_get, client):
    response = client.get("/league-matches?league=39")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "response" in data
    assert len(data["response"]) == 1

def test_league_matches_no_league(client):
    response = client.get("/league-matches")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data

@patch("requests.get", side_effect=mock_requests_get_league_info)
def test_league_info_success(mock_get, client):
    response = client.get("/league-info?league=39")
    data = json.loads(response.data)
    assert response.status_code == 200
    assert "response" in data
    assert data["response"][0]["league"]["id"] == 39

def test_league_info_no_league(client):
    response = client.get("/league-info")
    assert response.status_code == 400
    data = json.loads(response.data)
    assert "error" in data
