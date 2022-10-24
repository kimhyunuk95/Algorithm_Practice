T = 10

for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int,input().split()))
    cnt = 0
    for i in range(2,N-2):
        for j in range(height[i]):
            if height[i]-j > height[i-1] and height[i]-j > height[i-2] and height[i]-j > height[i+1] and height[i]-j > height[i+2]:
                cnt += 1
    print(f'#{test_case}',cnt)
    
    # -2-1 1 2 의 높이를 전부 체크해주면 쉽게 풀리는 문제
