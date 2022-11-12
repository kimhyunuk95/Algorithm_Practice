import sys
sys.setrecursionlimit(10000)

def dfs(v):
    visit[v] = True
    for i in graph[v]:
        if not visit[i]:
            dfs(i)

n, m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visit = [False]*(n+1)
cnt = 0 

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    if not visit[i]:
        dfs(i)
        cnt += 1

print(cnt)

# python은 재귀의 깊이가 1000으로 제한되어 있기 떄문에 sys.setrecursionlimit()을 이용해 바꾸어 주어야한다.
# pypy3로 제출해야 시간초과가 되지 않는다.
