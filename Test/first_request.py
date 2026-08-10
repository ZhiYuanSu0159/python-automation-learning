import requests

#0730破解了pythoncharm 初步使用pycharm，使用request发送请求查看响应

# 目标地址，相当于 Postman 里的 URL
url = "https://jsonplaceholder.typicode.com/posts/2"

# 发送 GET 请求
response = requests.get(url)

# 打印状态码
print("状态码:", response.status_code)


print("帖子标题",response.json()['title'])

# 打印响应 JSON
print("响应内容:")
print(response.json())