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

# PUT 请求测试一次就写对了，而且加了参数化
#
# DELETE 踩了一个小坑（多余参数），但这个坑会让你以后更仔细阅读函数签名
#
# 补全了 HTTP 四大方法，现在 GET、POST、PUT、DELETE 都能用 Python 自动化测试了

UPDATE_DATA = [
    {"title": "1", "body": "1", "userId": 1},
]
@pytest.mark.parametrize("update_payload", UPDATE_DATA)
def test_update_post(update_payload):
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_payload)
    data = response.json()
    assert response.status_code == 200, "不是200"
    assert data["title"] == update_payload["title"], "title替换失败"
    assert data["body"] == update_payload["body"], "body替换失败"
    assert data["id"] == 1

def test_delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    print("response.json()",response.json())