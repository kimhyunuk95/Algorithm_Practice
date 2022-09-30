C = int(input())
for _ in range(C):
    N = list(map(int, input().split()))
    sum = 0
    cnt = 0
    result = 0
    for i in range(1, len(N)):
        sum += N[i]
    avg = sum/N[0]
    for i in range(1, len(N)):
        if N[i] > avg:
            cnt += 1
    result = round((cnt/N[0])*100,5)
    print('{:.3f}%'.format(result))
