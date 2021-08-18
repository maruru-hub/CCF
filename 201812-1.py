# @Time    : 2021/7/6 10:31
# @Author  : maruru
import time
lr,ly,lg=input().split()    #分别代表三个灯的时长
lr,ly,lg=int(lr),int(ly),int(lg)    #三个变量变为整型
n=int(input())      #读入n
ti=0
start = time.time()
for i in range(n):
    #读入n次路况信息
    k,t=input().split()
    k,t=int(k),int(t)
    #一段道路直接加上时间
    if k==0:
        ti+=t
    #红灯时需要加上红灯的剩余秒数
    if k==1:
        ti+=t
    #黄灯是需要加上黄灯的剩余秒数和红灯的所有秒数
    if k==2:
        ti+=(t+lr)
    #绿灯时直接通过，不需要加时间
    if k==3:
        pass
end = time.time()
print(end-start)
print(ti)