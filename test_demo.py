import requests

#今日20260803了解使用pytest执行脚本，感受了下失败提示，理解pytest执行逻辑，需要test_函数或者类方法中包裹


def test_get_post_status_code():
    """验证 GET 请求返回 200 状态码"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    assert response.status_code == 200

def test_get_post_response_is_json():
    """验证返回数据可以被解析为 JSON"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()
    assert isinstance(data, dict), "返回内容不是 JSON 对象"

def test_get_post_has_required_fields():
    """验证返回数据包含必要的字段"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_get_post_id_correct():
    """验证请求 id=1 时返回的帖子 id 为 1"""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    data = response.json()
    assert data["id"] == 1