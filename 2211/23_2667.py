from collections import deque


n = int(input())
map = [list(map(int,input())) for i in range(n)]
d = [(-1,0), (1, 0), (0, -1), (0, 1)]
q = deque()
def bfs(map, a, b):
    count = 1
    q.append((a,b))
    map[a][b] = 0
    while q:
        x, y = q.popleft()
        for k in range(4):
            dx = x + d[k][0]
            dy = y + d[k][1]
            if 0 <= dx < n and 0 <= dy < n:
                if map[dx][dy] == 1:
                    map[dx][dy] = 0
                    q.append((dx, dy))
                    count += 1
    return count

cnt = []
for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            cnt.append(bfs(map, i, j))
        
cnt.sort()
print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])
    
    
 # dfs로도 풀어볼 것
