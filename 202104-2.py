# @Time    : 2021/8/4 13:23
# @Author  : maruru

# 图像长宽皆为n个像素，像素值<L,  领域范围为r, 均值<=t则为较暗区域
n, L, r, t = map(int, input().split(' '))
img = [[]] * n #图像矩阵
for i in range(n):
    img[i] = input().split(' ')
    for j in range(n):
        img[i][j] = eval(img[i][j])

def neigh(i,j):
    # 计算A_ij像素的领域像素均值
    xm = 0 if i-r<0 else i-r
    ym = 0 if j-r<0 else j-r
    xM = n-1 if i+r>n-1 else i+r
    yM = n-1 if j+r>n-1 else j+r
    s = 0
    for i in range(xm, xM+1):
        for j in range(ym, yM+1):
            s+=img[i][j]
    s/=((xM-xm+1)*(yM-ym+1))
    return s
bla = 0 # 处于较暗区域的像素数量
for i in range(n):
    for j in range(n):
        pix = neigh(i,j)
        print(pix)
        if pix<=t:
            bla+=1
print(bla)