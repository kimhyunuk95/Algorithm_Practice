def sol(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else :
        return sol(n-1) + sol(n-2) +sol(n-3)


T = int(input())

for _ in range(T):
    n = int(input())
    print(sol(n))
    
    
# 해답을 풀어서 써보면 n이 3보다 클 때(n>3), f(n) = f(n-1) + f(n-2) + f(n-3) 라는 점화식이 성립한다.
# 참조 : https://yongku.tistory.com/m/1273
