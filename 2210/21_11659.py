import sys
input = sys.stdin.readline
 
n, m = map(int, input().split())
arr = list(map(int, input().split()))
prefix_sum = [0]    # init prefix_sum    
 
temp = 0    
for i in arr:    # accumulate arr section 
    temp += i
    prefix_sum.append(temp)
 
for i in range(m):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])



# 아래와 같이 단순히 리스트로 구현하게 되면 시간초과가 나온다.(O(NM))
# 위와 같이 각각의 누적합을 저장해두었다가 빼주기만하면 O(1)이 되고 N개의 데이터와 M개의 입력이 있을때, O(N+M)의 시간이 보장된다.
# 참고 : https://ywtechit.tistory.com/79

# import sys

# N, M = map(int,sys.stdin.readline().rstrip().split())
# arr = list(map(int,sys.stdin.readline().rstrip().split()))
# sum = 0


# for _ in range(M):
#     sum = 0
#     i, j = map(int,sys.stdin.readline().rstrip().split())
#     for k in range(i-1,j,1):
#         sum += arr[k]
#     print(sum) 

