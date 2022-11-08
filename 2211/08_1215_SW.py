T = 10

for test_case in range(1, T+1):
    n = int(input())
    strList = [list(map(str,input())) for _ in range(8)]
    cnt = 0
    for i in range(8-n+1):
        for j in range(8):
            tmp = strList[j][i:i+n]
            if tmp == tmp[::-1]:
                cnt += 1
            for k in range(n//2):
                if strList[i+k][j] != strList[n+i-1-k][j]:
                    break
            else:
                cnt += 1
    print(cnt)
