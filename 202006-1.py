# @Time    : 2021/8/7 15:41
# @Author  : maruru

def issep(t1, t2, t3):
    temp = True
    A = []
    B = []
    for i in range(n):
        s = (t1 + coord[i][0] * t2 + coord[i][1] * t3)
        if s>0:
            A.append(i)
        else:
            B.append(i)
    t = A[0]
    for i in A:
        if coord[i][2]==coord[t][2]:
            continue
        else:
            temp = False
            break
    t = B[0]
    for i in B:
        if coord[i][2]==coord[t][2]:
            continue
        else:
            temp = False
            break

    return temp

n, m = map(int, input().split(' '))
# n, m分别代表点和查询的个数
coord = []
for i in range(n):
    coord.append(list(input().split(' ')))
    for j in range(2):
        coord[i][j] = int(coord[i][j])

theta = []
for i in range(m):
    theta.append(list(map(int, input().split(' '))))



for i in range(m):
    if issep(theta[i][0], theta[i][1], theta[i][2]):
        print('Yes')
    else:
        print('No')