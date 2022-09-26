N = int(input())
answer = 0
if N == 4 or N==7:
    print(-1)
else:
    while N%5 != 0:
        N = N - 3
        answer = answer + 1
    answer += N/5
    print(round(answer))
