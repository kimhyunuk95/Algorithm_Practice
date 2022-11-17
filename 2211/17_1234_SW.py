T = 10

for test_case in range(1, T+1):
    n, arr = map(int,input().split())
    arr = str(arr)
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
            continue
        if arr[i] != answer[-1]:
            answer.append(arr[i])
        else:
            answer.pop()
    ans = ""
    for a in answer:
        ans += a
    ans = int(ans)
    print(f'#{test_case}', ans)
