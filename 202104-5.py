# @Time    : 2021/8/13 20:41
# @Author  : maruru
# m, n = map(int, input().split(' '))
# # m条物流路线，n个物流站点
# load = []
# for i in range(m):
#     load.append(list(map(int, input().split(' '))))

def matrix(lst, n):
    mat = [[0]*n for _ in range(n)]
    for l in lst:
        point = [l[2*i+1] for i in range(l[0])]
        weight = [l[2*i] for i in range(1, l[0]+1)]
        for i in range(len(point)):
            mat[point[i]-1][point[(i+1)%len(point)]-1] = weight[i]
            mat[point[(i+1)%len(point)]-1][point[i]-1] = weight[i]

    return mat

lst = [[3,1,100,2,100,3,100], [3, 3, 100, 4, 100, 5, 100]]
n = 5
print(matrix(lst, n))
