def pow(a,b):
    if b == 1:
        return a
    ans = a*pow(a,b-1)
    return ans


T = 10

for test_case in range(1, T+1):
    n = int(input())
    a,b = map(int,input().split())
    ans = pow(a,b)
    print(f'#{test_case}',ans)
