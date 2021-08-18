# @Time    : 2021/8/11 10:27
# @Author  : maruru
import copy

def _NOT(ll):
    if not ll[0]:
        return 1
    else:
        return 0

def _AND(ll):
    st = ll[0]
    for i in range(1, len(ll)):
        st = st and ll[i]
    return st

def _OR(ll):
    st = ll[0]
    for i in range(1, len(ll)):
        st = st or ll[i]
    return st

def XOR(ll):
    st = ll[0]
    for i in range(1, len(ll)):
        st = st ^ ll[i]

def _NAND(ll):
    return _NOT([_AND(ll)])

def _NOR(ll):
    return _NOT([_OR(ll)])

# 构建邻接矩阵
def buildmatrix(temfunc):
    mat = [[0] * len(temfunc) for _ in range(len(temfunc))]
    for i in range(len(temfunc)):
        for j in range(2, int(temfunc[i])):
            if temfunc[i][j][0] == 'O':
                mat[int(temfunc[i][j][1:]) - 1][i] = 1  # On表示第n(列)个器件的输出连入到此端口(行)
    return mat

# 判断是否存在环
def findcircle(G):
    node_set = set()
    r = len(G)
    have_in_zero = True
    while have_in_zero:
        have_in_zero = False
        for i in range(r):
            if i not in node_set and not any([row[i] for row in G]):
                node_set.add(i)
                G[i] = [0] * r
                have_in_zero = True
                break
    return False if len(node_set) == r else True

def light(S, M, B, ip, op, func):
    res = []
    for i in range(S):
        I = {}
        O = {}




count = int(input())
fin = []
for _ in range(count):
    M, N = map(int, input().split())
    func = []
    ip = []
    op = []
    for _ in range(N):
        # 加一个状态值，判断有没有执行
        temp_func = list(map(str, input().split()))
        temp_func.append(True)
        func.append(temp_func)

    S = int(input())
    # 接下来S行有M个为0或1的数字，表示各个输入信号的状态
    for _ in range(S):
        ip.append(list(map(int, input().split())))
    # 接下来S行为输出行为输出描述
    for _ in range(S):
        op.append(list(map(int, input().split())))
    # 判断电路是否存在环路
    if findcircle(buildmatrix(func)):
        fin.append("LOOP")
        continue
    fin.append()