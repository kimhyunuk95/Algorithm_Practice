T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    result = {
        2:0,
        3:0,
        5:0,
        7:0,
        11:0
    }
    print(f'#{test_case}', end=" ")
    for key, val in result.items():
        while n % key ==0:
            result[key] += 1
            n /= key
        print(result[key], end=" ")
    print("")
