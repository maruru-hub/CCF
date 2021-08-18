# @Time    : 2021/8/6 10:36
# @Author  : maruru
# 输入安全指数数量
m = int(input())

# 初始化 y,result 存储列表
y_result = []

# 循环输入 y,result
for i in range(m):
    y_result.append(list(map(int,input().split())))

# 先按照result排序再按照y排序 避免使用同一y的最大predict
y_result.sort(key=lambda x:x[1],reverse=True) # 指定第二个元素进行排序
y_result.sort(key=lambda x:x[0])

# 构建存储predict正确数量的列表
count_Ture = []

# 正序遍历计算所有元素位置前 0 的个数(预测正确)
count = 0
for i in range(m):
    count_Ture.append(count)
    if y_result[i][1] == 0:
        count += 1

# 倒序遍历计算所有元素位置后 1 的个数(预测正确)
count = 0
for i in range(m-1,-1,-1):
    if y_result[i][1] == 1:
        count += 1
    count_Ture[i] += count

# 存储predict正确数量列表倒序操作(保证相同predict时输出y较大的) 并计算最大正确数量的下标索引
count_Ture.reverse()
index = m - 1 - count_Ture.index(max(count_Ture))

# 输出最佳阈值
print(y_result[index][0])
