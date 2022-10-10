from collections import deque


def DFS(graph, root):
    visited = []
    stack = [root]
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n])-set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)


def recursive_dfs(root,visited=[]):
    visited.append(root)
    for w in graph[root]:
        if not w in visited:
            visited = recursive_dfs(w, visited)
    return visited




def BFS(graph, root):
    visited = []
    queue = deque([root])
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)


graph = {}
n = input().split()
node, edge, start = [int(i) for i in n]
for i in range(edge):
    edge_info = input().split()
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

# print(recursive_dfs(start))
print(DFS(graph, start))
print(BFS(graph, start))

# 깊스넓큐 DFS는 스택 BFS는 큐
# DFS는 재귀함수로도 구현이 가능하다.
# 참고 : https://youtu.be/_hxFgg7TLZQ  
# https://cyc1am3n.github.io/2019/04/26/bfs_dfs_with_python.html 
# https://devyuseon.github.io/algorithm/dfs-and-bfs/
