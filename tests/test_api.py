import pytest


def test_get_posts_placeholder(api_context):
    # Playwright ya sabe que la base_url es JSONPlaceholder
    response = api_context.get("/posts/1")

    assert response.ok
    assert response.status == 200

    body = response.json()
    assert body["id"] == 1
    print(f"\nAPI Success: {body['title']}")


def test_create_post_placeholder(api_context):
    payload = {
        "title": "QA Gokay",
        "body": "Estructura final del framework",
        "userId": 1
    }

    response = api_context.post("/posts", data=payload)

    assert response.status == 201
    assert response.json()["title"] == "QA Gokay"
