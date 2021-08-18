# @Time    : 2021/8/17 14:26
# @Author  : maruru
n = eval(input())
jump = [0, 0, 0, 0]
num=[]
for i in range(1,n+1):
    num.append(i)
for i in num:
    if i%7==0 or ('7' in str(i)):
        no = i%4
        jump[no-1] += 1
        num.append(num[-1]+1)
    else:
        continue
for i in jump:
    print(i)