def GCD(a, b):
    if b% a: return GCD(b % a, a)
    else : return a

n, m = map(int, input().split(':'))
a = GCD(n, m)
print(n//a, end='')
print(":", end='')
print(m//a, end='')

# split을 통해 문자열 파싱을 한 후 유클리드 호제법을 사용하면 간단한 문제.
