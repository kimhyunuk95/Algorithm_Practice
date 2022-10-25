T = int(input())

for test_case in range(1, T+1):
    N, M = map(int,input().split())
    map_list = [list(map(int,input().split())) for _ in range(N)]
    total = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            answer = 0 
            for k in range(M):
                for l in range(M):
                    answer += map_list[i+k][j+l] 
                    if total < answer :
                        total = answer
    print(f'#{test_case}', total)
