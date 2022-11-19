T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    minimum = []

    for i in range(7):
        res = 0
        start = i
        cnt = 0
        while True:
            if res == n:
                break
            if arr[(start+cnt)%7] == 1:
                res += 1
            cnt += 1
        minimum.append(cnt)
         
    print(f'#{test_case}',min(minimum))
