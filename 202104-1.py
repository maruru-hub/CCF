# @Time    : 2021/8/4 10:09
# @Author  : maruru

'''

'''
n, m, L = map(int, input().split(' ')) # n行m列，L个灰度值
gray = [0]*L
for i in range(n):
    temp = input().split(' ')
    for j in range(m):
        temp[j] = int(temp[j])
        gray[temp[j]] += 1

for i in range(L):
    print(gray[i], end=' ')