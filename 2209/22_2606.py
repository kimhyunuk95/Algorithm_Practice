cptn = int(input())
m = int(input())
graph = [[] for _ in range(cptn+1)]
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)
  
 
def dfs(graph, start_node):
  visited, need_visited = list(), list()
  need_visited.append(start_node)
  while need_visited:
    node = need_visited.pop()
    if node not in visited:
      visited.append(node)
      if len(graph[node]) == 0:
        continue
      else:
        need_visited.extend(graph[node])
    return len(visited) -1
  
print(dfs(graph,1))


# 참고 : https://www.acmicpc.net/board/view/92980
