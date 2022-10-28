n = int(input())
d = [0] *1001
d[0] = 1
d[1] = 1
for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]
    d[i] %= 10007
print(d[n])

# n=1 일때 1 n=2일때 2 n=3 일때 3 n=4 일때 5 이므로 n = (n-1) + (n-2) 라는 점화식을 얻을 수 있다.
# 아래와 같이 재귀로 풀이하면 recursionerror가 나게된다.
# def sol(n):
#     ans = 0
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         ans = sol(n-1) + sol(n-2)
#     return ans


# n = int(input())
# ans = 0
# ans = sol(n)
# print(ans%10007)
