import sys

a, b, c = map(int,sys.stdin.readline().split())

def multi (a,n):
    if n == 1:
        return a%c
    else :
        tmp = multi(a, n//2)
        if n%2 == 0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c

print(multi(a,b))

# 당연하게도 math를 사용하면 시간 초과가 난다.
# 지수  법칙 A^(m+n) = A^m * A^n
# 나머지 분배 법칙 (A*B)%C = ((A%C)*(B%C))%C
