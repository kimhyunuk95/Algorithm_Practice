N = int(input())

list_number =[(int(input())) for i in range(N)]

list_number.sort()
for i in range(N):
    print(list_number[i])
    
# python3 로 제출하면 시간초과가 되어 pypy3로 제출하였다.
# python3로 제출할때 input() 대신 sys.stdin.readline()을 사용하면 통과가 된다.
