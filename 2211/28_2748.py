n = int(input())
dp = [0] * (n+1)
dp[0] = 0
dp[1] = 1
for i in range(2,n+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])


# 전형적인 dp문제
# 일반적인 풀이방법인 재귀방식으로 풀게되면 시간 초과가 난다
# 메모이제이션을 통해 시간을 줄여준다.
