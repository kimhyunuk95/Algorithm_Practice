T = 10

for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    while arr[7]!=0:
        for i in range(1,6):
            num = arr.pop(0)
            if (num-i) <= 0:
                arr.append(0)
                break
            arr.append(num-i)
    print(f'#{test_case}',end=' ')
    for i in range(8):
        print(arr[i], end=' ')
    print()
