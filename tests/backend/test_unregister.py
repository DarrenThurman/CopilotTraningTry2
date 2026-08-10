from src.app import activities


def test_unregister_participant_removes_email(client):
    # Arrange
    activity_name = "Chess Club"
    email = "student@example.com"
    activities[activity_name]["participants"] = [email]

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]
