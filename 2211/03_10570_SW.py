import math
T = int(input())

for test_case in range(1, T+1):
    a, b = map(int,input().split())
    cnt = 0
    num = 0
    for i in range(a,b+1):
        if str(i) == str(i)[::-1]:
            num = math.sqrt(i)
            if num.is_integer():
                if str(int(num)) == str(int(num))[::-1]:
                    cnt += 1
    print(f'#{test_case}',cnt)
