import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)


assert response.status_code == 200, f"状态码错误，预期200实际{response.status_code}"

data = response.json()

assert "userId" in data, "返回数据缺少userID"
assert "id" in data, "返回数据缺少 id 字段"
assert "title" in data, "返回数据缺少 title 字段"
assert "body" in data, "返回数据缺少 body 字段"


assert data["id"] == 1,f"帖子 id 错误，预期1，实际{data['id']}"

print("PASS")
print(f"帖子标题: {data['title']}")