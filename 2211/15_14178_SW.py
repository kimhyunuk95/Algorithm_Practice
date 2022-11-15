T = int(input())

for test_case in range(1, T+1):
    n, d = map(int,input().split())

    cover = (d * 2) +1
    if (n % cover) > 0:
        print(f'#{test_case}', n//cover +1)
    else :
        print(f'#{test_case}', n//cover)
