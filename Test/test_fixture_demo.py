import pytest
import requests

@pytest.fixture
def get_post_response():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    return response

def test_status(get_post_response):
    assert get_post_response.status_code == 200

def test_get_post_has_required_fields(get_post_response):
    data = get_post_response.json()
    assert "userId" in data
    assert "title" in data
    assert "body" in data
    assert "id" in data

def test_get_post_has_response_is_json(get_post_response):
    data = get_post_response.json()
    assert isinstance(data, dict),"返回内容不是json对象"

def test_get_post_id_correct(get_post_response):
    data = get_post_response.json()
    assert data["id"] == 1