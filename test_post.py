import pytest
import requests
# 第六天收获：学会了用 requests.post(json=) 发送创建请求，
# 断言状态码 201，并用参数化跑不同 body 数据。
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