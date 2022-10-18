N, K = map(int,input().split())
value = list()
cnt = 0
count = 0
for _ in range(N):
    value.append(int(input()))
    value.sort(reverse=True)
for i in value:
    if i <= K:
        count = K // i
        K = K - i*count
        cnt += count

print(cnt)
