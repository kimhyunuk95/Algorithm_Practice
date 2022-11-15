from collections import deque

n, m = map(int,input().split())
box = [list(map(int,input().split())) for _ in range(m)]

d = [(-1,0),(1, 0), (0,-1), (0, 1)]
ans = 0
q = deque()
def bfs():
    while q:
        x, y = q.popleft()
        for i in range(len(d)):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < m and 0 <= dy < n and box[dx][dy] == 0:
                box[dx][dy] = box[x][y] + 1
                q.append([dx,dy])

for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            q.append([i,j])
# 1이 여러개인 경우가 있으므로 모든 1을 q에 append 하는 것이 포인트

bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)
