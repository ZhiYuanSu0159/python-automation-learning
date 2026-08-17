import allure
import pytest
import requests
from pygments.lexers import data

from config.settings import SINGLE_POST_URL


@allure.feature("GET 请求测试")
class TestGetPost:

    @allure.story("查询单个帖子")
    @allure.title("验证码为200")
    def test_status(self, get_post_response):
        assert get_post_response.status_code == 200

    @allure.story("查询单个帖子")
    @allure.title("验证返回数据包含必要字段")
    def test_get_post_has_reuired_fields(self,get_post_response):
        data = get_post_response.json()
        assert "userId" in data
        assert "id" in data
        assert "title" in data
        assert "body" in data

    @allure.story("查询单个帖子")
    @allure.title("验证返回数据为JSON格式")
    def test_get_post_has_response_is_json(self, get_post_response):
        data = get_post_response.json()
        assert isinstance(data, dict)

    @allure.story("查询单个帖子")
    @allure.title("验证返回的帖子ID正确")
    def test_get_post_id_correct(self, get_post_response):
        data = get_post_response.json()
        assert data["id"] == 1

@pytest.fixture
def get_post_response():
    response = requests.get(SINGLE_POST_URL)
    return response


# pytest --alluredir=allure-results
# allure generate allure-results -o allure-report --clean
# allure open allure-report