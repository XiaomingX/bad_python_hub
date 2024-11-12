from queue import Queue

# 创建一个最大容量为3的队列
q = Queue(maxsize=3)

# 向队列中添加元素
q.put('苹果')
q.put('香蕉')
q.put('樱桃')

# 检查队列是否已满
print("队列是否已满:", q.full())  # 输出: True

# 从队列中移除元素
print("从队列中移除的元素:", q.get())  # 输出: '苹果'
print("从队列中移除的元素:", q.get())  # 输出: '香蕉'

# 检查当前队列的大小
print("当前队列大小:", q.qsize())  # 输出: 1

# 再次添加一个元素
q.put('橙子')

# 检查队列是否为空
print("队列是否为空:", q.empty())  # 输出: False

# 移除剩余的元素
print("从队列中移除的元素:", q.get())  # 输出: '樱桃'
print("从队列中移除的元素:", q.get())  # 输出: '橙子'

# 检查队列是否为空
print("队列是否为空:", q.empty())  # 输出: True