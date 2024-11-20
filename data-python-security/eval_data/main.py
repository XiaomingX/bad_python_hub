import json
import os

# 模拟用户输入的数据
data = "__import__('os').system(\"echo '# Hello, Markdown!' > hello.md\")"

def main():
    # 直接在 eval 中使用用户可控的数据
    item_dict = json.loads(json.dumps(eval(data)))

if __name__ == "__main__":
    main()
