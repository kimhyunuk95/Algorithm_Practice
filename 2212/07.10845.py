from collections import deque
import sys

q = deque()
n = int(sys.stdin.readline()) # 시간초과가 나와서 input보다 속도가 빠른 readline을 사용했다.
for _ in range(n):
    wrd = list(map(str,sys.stdin.readline().split())) 
    # list로 입력받아 push 일때는 2개가 입력되는 것을 처리해준다. wrd[0] = 명령어 wrd[1] = 숫자
    if wrd[0] == 'push':
        q.append(int(wrd[1]))
    elif wrd[0] == 'pop':
        if not q:
            # q가 비어있을 경우
            print(-1)
        else:
            tmp = q.popleft()
            print(tmp)
    elif wrd[0] == 'size':
        print(len(q))
    elif wrd[0] == 'empty':
        if not q :
            print(1)
        else :
            print(0)
    elif wrd[0] == 'front':
        if not q :
            print(-1)
        else:
            print(q[0])
    elif wrd[0] == 'back':
        if not q :
            print(-1)
        else:
            print(q[-1])
