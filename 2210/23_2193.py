N = int(input())
dp = [0,1,1]
for i in range(3,91):
    result = dp[i-1]+dp[i-2]
    dp.append(result)

print(dp[N])

# 직접 구해보면 0,1,1,2,3,6,9...이 나오게 된다 여기서 4번째 숫자부터 식 (i-1)+(i-2)를 만족함을 알 수 있다.
