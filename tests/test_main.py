from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Dandy's World" in response.text
    assert "student-name-input" in response.text
    assert "container-s2-questions" in response.text
    assert "container-s4-builder" in response.text
    assert "SENTENCE_BUILDER_ITEMS" in response.text
    assert "s2_questionsShortAnswers" in response.text
    assert "IN FRONT OF" in response.text


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["domain"] == "english.hurlingham.xyz"


def test_pdf_endpoint():
    response = client.get("/pdf")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"


def test_static_assets():
    for toon in [
        "dandy.png",
        "poppy.png",
        "pebble.png",
        "flutter.png",
        "sprout.png",
        "astro.png",
        "boxten.png",
        "goob.png",
        "cosmo.png",
        "shrimpo.png",
        "vee.png",
    ]:
        response = client.get(f"/static/dandy_assets/{toon}")
        assert response.status_code == 200
        assert "image/png" in response.headers["content-type"]

    town_resp = client.get("/static/dandy_assets/gardenview_town.jpg")
    assert town_resp.status_code == 200
    assert "image/jpeg" in town_resp.headers["content-type"]
