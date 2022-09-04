import math

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    answer = math.factorial(M) / (math.factorial(M-N) * math.factorial(N))
    print(int(answer))
    
    
    
# 이 문제는 조합을 이용하여 간단하게 해결 할 수 있는 문제이다.
# python에는 이미 팩토리얼이 구현되어있는 라이브러리가 있으므로 구현하지 않았다.
