import json
import os
import copy

# 模拟数据库的JSON文件
DB_FILE = "database.json"

# 初始数据
INITIAL_DATA = {
    "posts": [
        {"id": 1, "title": "First Post", "body": "This is the first post", "userId": 1},
        {"id": 2, "title": "Second Post", "body": "This is the second post", "userId": 1},
    ]
}

def init_db():
    """如果数据库文件不存在，创建一个"""
    if not os.path.exists(DB_FILE):
        with open(DB_FILE, "w") as f:
            json.dump(INITIAL_DATA, f, indent=2)

def read_db():
    """读取整个数据库"""
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_db(data):
    """写入整个数据库"""
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=2)

# ========== CRUD 操作（模拟你的接口测试对象） ==========

def get_post(post_id):
    """GET：查询单条"""
    db = read_db()
    for post in db["posts"]:
        if post["id"] == post_id:
            return {"status": "found", "data": post}
    return {"status": "not_found", "data": None}

def create_post(title, body, user_id):
    """POST：新增"""
    db = read_db()
    new_id = max(post["id"] for post in db["posts"]) + 1 if db["posts"] else 1
    new_post = {"id": new_id, "title": title, "body": body, "userId": user_id}
    db["posts"].append(new_post)
    write_db(db)
    return {"status": "created", "data": new_post}

def update_post(post_id, title, body, user_id):
    """PUT：完整更新（替换所有字段）"""
    db = read_db()
    for post in db["posts"]:
        if post["id"] == post_id:
            post["title"] = title
            post["body"] = body
            post["userId"] = user_id
            write_db(db)
            return {"status": "updated", "data": post}
    return {"status": "not_found", "data": None}

def delete_post(post_id):
    """DELETE：删除"""
    db = read_db()
    for i, post in enumerate(db["posts"]):
        if post["id"] == post_id:
            deleted = db["posts"].pop(i)
            write_db(db)
            return {"status": "deleted", "data": deleted}
    return {"status": "not_found", "data": None}

# ========== 初始化数据库 ==========
init_db()