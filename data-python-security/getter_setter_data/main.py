class FileCreator:
    def __init__(self):
        self.create_trigger = False

    def __getattr__(self, name):
        if name == 'create_file':
            # 当访问不存在的 'create_file' 属性时，触发文件创建
            self._create_file()
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{name}'")

    def __setattr__(self, name, value):
        # 利用 setattr 来创建文件
        if name == 'create_trigger' and value is True:
            self._create_file()
        super().__setattr__(name, value)

    def _create_file(self):
        with open('hahaha.md', 'w') as file:
            file.write('# This is hahaha.md\nFile created due to getattr or setattr misuse.')

# 使用 getattr 和 setattr 进行滥用的示例
creator = FileCreator()

# 触发创建文件的方法1：尝试访问不存在的属性 'create_file'
try:
    creator.create_file
except AttributeError:
    pass

# 触发创建文件的方法2：将 'create_trigger' 设置为 True
creator.create_trigger = True
