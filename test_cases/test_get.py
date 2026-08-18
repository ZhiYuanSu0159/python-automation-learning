import logging

import pytest
import requests
from pygments.lexers import data

from config.settings import SINGLE_POST_URL

#今日20260803了解使用pytest执行脚本，感受了下失败提示，理解pytest执行逻辑，需要test_函数或者类方法中包裹

@pytest.fixture
def get_post_response():
    url = SINGLE_POST_URL
    logging.info(f"开始请求：{url}")
    response = requests.get(SINGLE_POST_URL)
    logging.info(f"响应状态码：{response.status_code}")
    return response

# def test_get_post_status_code():
#     """验证 GET 请求返回 200 状态码"""
#     url = "https://jsonplaceholder.typicode.com/posts/1"
#     response = requests.get(url)
#     assert response.status_code == 200

def test_status(get_post_response):
    logging.info(f"开始测试状态码{get_post_response.status_code}")
    assert get_post_response.status_code == 200

def test_get_post_response_is_json(get_post_response):
    """验证返回数据可以被解析为 JSON"""
    # url = "https://jsonplaceholder.typicode.com/posts/1"
    # response = requests.get(url)
    # data = response.json()
    data = get_post_response.json()
    logging.info(f"开始测试返回数据类型{data}")
    assert isinstance(data, dict), "返回内容不是 JSON 对象"

def test_get_post_has_required_fields(get_post_response):
    """验证返回数据包含必要的字段"""
    # url = "https://jsonplaceholder.typicode.com/posts/1"
    # response = requests.get(url)
    # data = response.json()
    logging.info(f"开始校验关键数据是否存在")
    data = get_post_response.json()
    assert "userId" in data
    assert "id" in data
    assert "title" in data
    assert "body" in data

def test_get_post_id_correct(get_post_response):
    """验证请求 id=1 时返回的帖子 id 为 1"""
    # url = "https://jsonplaceholder.typicode.com/posts/1"
    # response = requests.get(url)
    # data = response.json()
    data = get_post_response.json()
    assert data["id"] == 1