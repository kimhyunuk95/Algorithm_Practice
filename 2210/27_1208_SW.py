T = 10

for test_case in range(1, T+1):
    dump = int(input())
    height = list(map(int,input().split()))
    result = 0
    for j in range(dump):
        max_idx = height.index(max(height))
        min_idx = height.index(min(height))
        height[max_idx] -= 1
        height[min_idx] += 1

    result = max(height) - min(height)
    print(f'#{test_case}', result)
