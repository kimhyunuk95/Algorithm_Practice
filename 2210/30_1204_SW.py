from collections import Counter

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    arr = list(map(int,input().split()))
    mc = Counter(arr).most_common(1)
    print(f'#{test_case}',max(max(mc)))
