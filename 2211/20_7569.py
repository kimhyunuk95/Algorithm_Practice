from collections import deque
import sys
m, n, h = map(int,input().split())
q = deque()
box = []

for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                q.append([i,j,k])
    box.append(tmp)

ax = [-1,1,0,0,0,0]
by = [0,0,-1,1,0,0]
cz = [0,0,0,0,-1,1]


while q:
    x, y, z = q.popleft()
    for i in range(6):
        dx = x + ax[i]
        dy = y + by[i]
        dz = z + cz[i]
        if 0 <= dx < h and 0 <= dy < n and 0 <= dz < m:
            if box[dx][dy][dz] == 0:
                box[dx][dy][dz] = box[x][y][z] + 1
                q.append([dx,dy,dz])

day = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit()
        day = max(day,max(j))
print(day-1)

# 참조 : https://jiwon-coding.tistory.com/98
