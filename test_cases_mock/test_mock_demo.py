# 第十天收获：用 Mock 模拟接口返回，测试不再依赖外部网络，速度更快更稳定。

import pytest
import requests
from unittest.mock import patch, Mock

def get_mock_data(id):
    url = f"http://api.gettest.com/{id}"
    response = requests.get(url)
    data = response.json()
    return f"The ID is {id} The body is {data['body']}"

class TestGetPost:
    def test_get(self):
        fake_response = Mock()
        fake_response.json.return_value = {"body": "hello"}
        with patch('requests.get', return_value=fake_response) as mock_get:
            result = get_mock_data("123")
            assert result == "The ID is 123 The body is hello"
            mock_get.assert_called_once_with("http://api.gettest.com/123")





def test_mock_get_request():
    """使用 Mock 模拟 requests.get，不真正访问网络"""
    # 创建一个假的响应对象
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "userId": 1,
        "id": 999,
        "title": "mock title",
        "body": "mock body"
    }

    # 用 patch 替换 requests.get
    with patch('requests.get', return_value=fake_response) as mock_get:
        response = requests.get("https://any-url.com")  # 这个请求不会真正发出

        # 断言
        assert response.status_code == 200
        data = response.json()
        assert data["title"] == "mock title"
        assert data["id"] == 999

        # 验证 requests.get 确实被调用了一次
        mock_get.assert_called_once()
