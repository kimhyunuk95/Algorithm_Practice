n = int(input())
arr = list(map(int,input().split()))
dp = [0]
dp[0] = arr[0]

for i in range(n-1):
    dp.append(max(arr[i+1], dp[i]+arr[i+1]))

print(max(dp))

# 다이나믹프로그래밍을 이용
# dp에 숫자배열에서 더한값과 더하지 않은값중에 더 큰 수를 넣어줌
