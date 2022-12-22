n, m = map(int,input().split())
answer = list()

def backTraking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        answer.append(i)
        backTraking(depth+1)
        answer.pop()

backTraking(0)

# 재귀함수를 이용한 완전탐색으로 백트래킹을 이용함.
