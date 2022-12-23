n, m = map(int,input().split())
answer = list()

def backTraking(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, n+1):
        if i in answer:
            continue
        # 현재 수열에 추가하고자 하는 값이 이미 있다면 다음 값으로 넘어간다.
        answer.append(i)
        backTraking(depth+1)
        answer.pop()

backTraking(0)

# 재귀함수를 이용한 백트래킹
