dp = [0] * 10001
glass = [0] * 10001

n = int(input())
for i in range(1,n+1):
    glass[i] = int(input())

dp[1] = glass[1]
dp[2] = glass[1] + glass[2]
for i in range(3,n+1):
    dp[i] = max(dp[i-1],dp[i-2]+glass[i], dp[i-3]+glass[i-1]+glass[i])
print(dp[n])

# dp를 이용한 풀이
# dp[1] = glass[1] -> 첫번째 위치에서 가장 많이 마시는 경우
# dp[2] = glass[1] + glass[2] -> 두번째 위치에서 가장 많이 마시는 경우
# dp[n] = max(dp[n-1], dp[n-2] + glass[n], dp[n-3] + glass[n-1] + glass[n]) -> n번째 위치에서 가장 많이 마시는 경우 (n>3)
# dp의 경우 점화식을 찾아내는 것이 가장 중요하다.
