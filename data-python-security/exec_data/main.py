class Vulnerable:
    def __init__(self):
        self.filename = None

    def __set_filename(self, name):
        self.filename = name

    def __create_file(self):
        if self.filename:
            with open(self.filename, 'w') as f:
                f.write("This file was created by misusing getattr, setattr, and exec.")

# 模拟恶意代码
malicious_code = """
# 获取对象实例
vuln_instance = target_instance

# 设置 filename 属性为 'hahaha.md'
setattr(vuln_instance, '_Vulnerable__set_filename', lambda x: x('hahaha.md'))

# 执行 __set_filename 方法来设置文件名
getattr(vuln_instance, '_Vulnerable__set_filename')(vuln_instance.__set_filename)

# 调用 __create_file 方法来创建文件
getattr(vuln_instance, '_Vulnerable__create_file')()
"""

# 执行代码示例
if __name__ == "__main__":
    # 创建易受攻击的对象
    target_instance = Vulnerable()

    # 使用 exec 以字符串方式执行恶意代码
    exec(malicious_code)

    print("恶意代码执行完毕，请检查当前目录是否存在 hahaha.md 文件。")
