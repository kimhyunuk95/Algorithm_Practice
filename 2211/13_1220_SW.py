T = 10

for test_case in range(1, T+1):
    n = int(input())
    table = [list(map(int,input().split())) for _ in range(100)]
    cnt = 0
    for i in range(n):
        check = 0
        for j in range(n):
            if check == 0 and table[j][i] == 1:
                check = 1
            if check == 1 and table[j][i] == 2:
                check = 0
                cnt += 1
    print(f'#{test_case}', cnt)
