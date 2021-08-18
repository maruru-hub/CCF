# @Time    : 2021/8/18 8:24
# @Author  : maruru
n = eval(input())
# n表示已查明的垃圾点个数
garbage = {}
score = [0 for _ in range(5)]
for i in range(n):
    temp = tuple(map(int, input().split(' ')))
    garbage[temp] = 0

for key in garbage:
    if (key[0], key[1]+1) in garbage and (key[0]+1, key[1]) in garbage and (key[0], key[1]-1) in garbage and (key[0]-1, key[1]) in garbage:
        s = 0
        for i in [1,-1]:
            for j in [1,-1]:

                if (key[0]+i, key[1]+j) in garbage:
                    s += 1
        score[s] +=1
    else:
        continue

for i in score:
    print(i)