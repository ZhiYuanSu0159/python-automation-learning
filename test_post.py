import pytest
import requests

POST_DATA = [
    {"title": "foo", "body": "bar", "userId": 1},
    {"title": "hello", "body": "world", "userId": 2},
    {"title": "test", "body": "自动化测试", "userId": 3},
]
@pytest.mark.parametrize("payload", POST_DATA)

def test_create_post(payload):
    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=payload)
    assert response.status_code == 201,"不是201"
    assert "title" in response.json()
    assert "body" in response.json()
    # 检查字段值是否与发送的数据一致
    assert response.json()["title"] == payload["title"]
    assert response.json()["body"] == payload["body"]
    assert response.json()["userId"] == payload["userId"]

   # jsonplaceholder 规则：新创建的 id 固定为 101
    assert response.json()["id"] == 101