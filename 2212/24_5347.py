def LCM(a, b):
    return (a * b) // GCD(a, b)

def GCD(a, b):
    if b % a : return GCD(b%a, a)
    else: return a
# 1) A와 B의 최대공약수를 구하기 위해 A를 B로 나눈 나머지 R1을 구한다.
# 2) B를 R1로 나눈 나머지 R2를 구한다.
# 3) R1을 R2로 나눈 나머지 R3을 구한다.
# 4) 1~3을 반복하여 어느 한쪽이 나누어 떨어질때 까지 한다. 나누어 떨어질 때
# 이 직전에 얻은 나머지가 최대 공약수가 된다.
n = int(input())
for i in range(n):
    a, b = map(int,input().split())
    print(LCM(a,b))

# 유클리드 호제법을 이용한다.
