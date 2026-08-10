from fastapi.testclient import TestClient

from src.app import activities, app


def test_unregister_participant_removes_email():
    activities["Chess Club"]["participants"] = ["student@example.com"]
    client = TestClient(app)

    response = client.delete(
        "/activities/Chess Club/participants",
        params={"email": "student@example.com"},
    )

    assert response.status_code == 200
    assert "student@example.com" not in activities["Chess Club"]["participants"]
    assert response.json()["message"] == "Unregistered student@example.com from Chess Club"
