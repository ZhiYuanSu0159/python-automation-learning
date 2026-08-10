import pytest
import requests
from urllib3 import request


# @pytest.fixture
# def fetch_post(post_id):
#     url = "https://jsonplaceholder.typicode.com/posts/" + str(post_id)
#     return requests.get(url)
#
# @pytest.mark.parametrize("post_id",[1,2,3,4,5])
# def test_post_fields0(post_id):
#     response = fetch_post(post_id)
#     data = response.json()
#     assert response.status_code == 200
#     assert "userId" in data
#     assert "title" in data
#     assert "body" in data
#     assert "id" in data
#     assert isinstance(data["userId"], int),"ID不是int"
#     assert isinstance(data,dict),"不是json"

# def fetch_post(post_id):
#     """根据 post_id 发送 GET 请求并返回 response"""
#     url = "https://jsonplaceholder.typicode.com/posts/" + str(post_id)
#     return requests.get(url)
#
#
# @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5])
# def test_post_fields(post_id):
#     response = fetch_post(post_id)
#     data = response.json()
#
#     assert response.status_code == 200
#     assert "userId" in data
#     assert "id" in data
#     assert "title" in data
#     assert "body" in data
#     assert isinstance(data["userId"], int), "userId 不是 int"
#     assert isinstance(data, dict), "不是 JSON"

@pytest.fixture
def post_response(request):
    """带参数的 fixture：通过 request.param 拿到参数"""
    post_id = request.param
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    resp = requests.get(url)
    return resp


@pytest.mark.parametrize("post_response", [1, 2, 3], indirect=True)
def test_post_advanced(post_response):
    data = post_response.json()
    assert post_response.status_code == 200
    assert data["id"] == post_response.json()["id"]  # 这里只是为了演示