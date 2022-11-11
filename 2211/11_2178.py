from collections import deque


n, m = map(int,input().split())
maze = [list(map(int,input())) for _ in range(n)]
d = [(-1,0), (1,0),(0,-1),(0,1)]
q = deque()
q.append((0,0))
def bfs():
    while q:
        x,y = q.popleft()
        for k in range(4):
            dx = x + d[k][0]
            dy = y + d[k][1]
            if 0 <= dx < n and 0 <= dy < m:
                if maze[dx][dy] == 1:
                    maze[dx][dy] = maze[x][y] + 1
                    q.append((dx,dy))
maze[0][0] = 1
bfs()
print(maze[n-1][m-1])
