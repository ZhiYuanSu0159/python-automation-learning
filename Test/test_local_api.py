import pytest
from local_api_simulator import (
    init_db, get_post, create_post, update_post, delete_post
)

@pytest.fixture(autouse=True)
def reset_db():
    """每个测试前重置数据库，保证测试独立性"""
    init_db()

def test_get_existing_post():
    """GET：查询存在的帖子"""
    result = get_post(1)
    assert result["status"] == "found"
    assert result["data"]["title"] == "First Post"

def test_get_nonexistent_post():
    """GET：查询不存在的帖子"""
    result = get_post(999)
    assert result["status"] == "not_found"

def test_create_post():
    """POST：创建新帖子"""
    result = create_post("New Title", "New Body", 2)
    assert result["status"] == "created"
    assert result["data"]["id"] == 3
    # 验证确实被创建了
    assert get_post(3)["status"] == "found"

def test_update_post():
    """PUT：完整更新帖子"""
    result = update_post(1, "Updated Title", "Updated Body", 10)
    assert result["status"] == "updated"
    # 验证更新后的值
    updated = get_post(1)["data"]
    assert updated["title"] == "Updated Title"
    assert updated["userId"] == 10

def test_delete_post():
    """DELETE：删除帖子"""
    result = delete_post(1)
    assert result["status"] == "deleted"
    # 验证确实被删除了
    assert get_post(1)["status"] == "not_found"

def test_delete_nonexistent_post():
    """DELETE：删除不存在的帖子"""
    result = delete_post(999)
    assert result["status"] == "not_found"