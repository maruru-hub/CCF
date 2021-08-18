# @Time    : 2021/8/16 19:40
# @Author  : maruru
from math import pi, cos, sin, acos
n, m = map(int, input().split(' '))
# n维空间, m个点
r = eval(input())
center = list(map(int, input().split(' ')))
# r为黑洞的半径
target = []
distance = [[0 for _ in range(m)] for _ in range(m)]  # 记录每个点到另外点的最短距离
C = 2*pi*r  # 黑洞的周长

# 注意此处的距离没有平方
def getDistance(x, y):
    s = 0
    for i in range(n):
        s += (x[i] - y[i])**2
    return s
def getSquare(a, b, c):
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    h = 2*s/c
    return h

def getShortDis(x, y):
    c = getDistance(x, y)
    c1 = c**0.5
    a = getDistance(x, center)
    a1 = a**0.5
    b = getDistance(y, center)
    b1 = b**0.5
    ctheta = (a + b - c)/(2*a1*b1)
    h = getSquare(a1, b1, c1)
    # 判断两点所成直线与黑洞圆的关系
    if h>r and ctheta>0:  # 所成角为锐角
        return (a+b)**0.5
    elif h == r:  # 正好相切
        theta = acos(ctheta)  #弧度制
        l = theta*r  #圆心角所对应的弧长
        return l
    else:
        x1 = (a-r**2)**0.5
        th1 = r/(a)**0.5
        x2 = (b-r**2)**0.5
        th2  = r/(b)**0.5
        theta = acos(ctheta)
        th = theta - acos(th1) - acos(th2)
        l = th*r
        return  (l+x1 + x2)



for i in range(m):
    loc = list(map(int, input().split(' ')))
    target.append(loc)

for i in range(m):
    for j in range(i+1, m):
        dis = getShortDis(target[i], target[j])
        distance[i][j] = distance[j][i] = dis

#print(distance)
for i in range(m):
    print("%.14f" %sum(distance[i]))
