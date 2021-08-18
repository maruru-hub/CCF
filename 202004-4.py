# @Time    : 2021/8/15 13:52
# @Author  : maruru
def getFactor(al, ar):
    fac = [1]
    lim = ar - al
    for i in range(2, lim//2+1):
        if lim%i==0:
            fac.append(i)
            fac.append(int(lim/i))
    return set(fac)

#print(set(getFactor(0,2)))

def tree(k):
    if dp[k] != 0:
        return dp[k]
    else:
        locc = set()
        s = 0
        for i in range(k-1, -1, -1):
            fac = getFactor(loc[i], loc[k])
            t = len(fac - locc)
            locc = (locc|fac)
            s += tree(i)*t
        dp[k] = s
        return dp[k]

n = eval(input())  #n表示障碍物的数量
loc = list(map(int, input().split(' '))) # 障碍物的坐标
dp = [0] * len(loc) # dp[i]表示前i个障碍物的方案
dp[0] = 1

#print(tree(1))
print(tree(n-1))
print(dp)