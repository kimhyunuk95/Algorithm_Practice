T = int(input())

for test_case in range(1,T+1):
    arr = input()
    a = 1
    b = 1
    for i in range(len(arr)):
        if arr[i] == 'L':
            a = a
            b = a + b
        elif arr[i] == 'R':
            a = a + b
            b = b
    print(f'#{test_case}', a, b)
