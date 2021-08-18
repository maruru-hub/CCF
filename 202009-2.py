# @Time    : 2021/8/6 14:56
# @Author  : maruru

n, k, t, xl, yd, xr, yu = map(int, input().split(' '))
location = [[]] * n

def iswait(x,y):
    if xl<=x<=xr and yd<=y<=yu:
        return True
    else:
        return False
# print(location)

for i in range(n):
    location[i] = input().split(' ')
    for j in range(2*t):
        location[i][j] = int(location[i][j])


s1 = s2 = 0
for i in range(n):
    count = max_count = 0  # 初始为不在高危区域
    for j in range(0, 2*t, 2):
        if iswait(location[i][j], location[i][j+1]):
            count+= 1
            if max_count <= count:
                max_count = count
        else:
            count = 0
    if max_count != 0:
        s1+=1
        if max_count >= k:
            s2 += 1

print(s1)
print(s2)

#############################################################
# # 输入n,k,t,xl,yd,xr,yu
# n, k, t, xl, yd, xr, yu = map(int, input().split())
#
# # 记录经过或逗留人数列表
# pass_stay = [0, 0]
#
# # 循环输入并判断
# for i in range(n):
#     seat = list(map(int, input().split()))
#
#     # 连续最多逗留时长和此次逗留时长初始化
#     max_count = 0
#     count = 0
#
#     # 遍历时间
#     for j in range(t):
#         # 判断是否处于区域内部
#         if xl <= seat[j * 2] and seat[j * 2] <= xr and yd <= seat[j * 2 + 1] and seat[j * 2 + 1] <= yu:
#             count += 1
#             # 判断是否更新最长逗留时间
#             if count > max_count:
#                 max_count = count
#         else:
#             count = 0
#
#     # 在经过高风险地区时 判断该居民始经过还是逗留
#     if max_count != 0:
#         if max_count < k:
#             pass_stay[0] += 1
#         else:
#             pass_stay[0] += 1
#             pass_stay[1] += 1
#
# # 输出结果
# print(pass_stay[0])
# print(pass_stay[1])
