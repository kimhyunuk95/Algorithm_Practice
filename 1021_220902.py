from collections import deque

N, M = map(int, input().split())
array = list(map(int, input().split()))
dq = deque([i for i in range(1, N+1)])
total = 0
for i in array:
    while True:
        if dq[0] == i:
            dq.popleft()
            break
        else:
            if dq.index(i) < len(dq)/2:
                while dq[0] != i:
                    dq.append(dq.popleft())
                    total += 1
            else:
                while dq[0] != i:
                    dq.appendleft(dq.pop())
                    total += 1
print(total)


# 참고 https://wiselog.tistory.com/126
