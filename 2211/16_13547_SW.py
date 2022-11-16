T = int(input())

for test_case in range(1, T+1):
    arr = str(input())
    cnt = 0
    for i in range(len(arr)):
        if arr[i] == 'x':
            cnt += 1
    if cnt <= 7:
        print(f'#{test_case} YES')
    else:
        print(f'#{test_case} NO')
