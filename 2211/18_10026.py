import sys
sys.setrecursionlimit(1000000)

n = int(input())
block = [list(map(str,input())) for _ in range(n)]
visit = [[False]*n for _ in range(n)]
thr_cnt, two_cnt = 0, 0
d = [(-1,0), (1,0), (0,-1), (0,1)]
def dfs(x,y):
    visit[x][y] = True
    current_color = block[x][y]
    for k in range(4):
        nx = x + d[k][0]
        ny = y + d[k][1]
        if 0 <= nx < n and 0 <= ny < n:
            if visit[nx][ny] == False:
                if block[nx][ny] == current_color:
                    dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            dfs(i,j)
            thr_cnt += 1

for i in range(n):
    for j in range(n):
        if block[i][j] == 'R':
            block[i][j] = 'G'
# 적색을 녹색으로 바꿔줌
# 블럭을 다시 세야하므로 visit을 초기화 함
visit = [[False]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visit[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(thr_cnt, two_cnt)
