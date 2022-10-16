import sys
M = int(sys.stdin.readline())
s = set()
for _ in range(M):
    line = list(sys.stdin.readline().strip().split())
    o = line[0]

    if len(line) == 1:
        if o == 'all':
            s.clear()
            s = set([i for i in range(1,21)])
        else:
            s.clear()

    else:
        x = int(line[1])
        if o == 'add':
            s.add(x)
        elif o == 'remove':
            s.discard(x)
        elif o == 'check':
            if x in s:
                print(1)
            else :
                print(0)
        elif o == 'toggle':
            if x in s:
                s.discard(x)
            else :
                s.add(x)
        
# 시간 초과가 많이 떴다. input을 쓰는 대신 sys를 import해서 readline을 쓰는 습관을 들여야 겠다.
# *input()은 마지막 개행문자를 포함하지 않음. readline()은 마지막 개행 문자를 포함함
