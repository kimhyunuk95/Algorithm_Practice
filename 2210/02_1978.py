N = int(input())
A = list(map(int,input().split()))
answer = [0]*N
def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x%i ==0:
            return False
    return True

for i in range(len(A)):
    answer[i] = is_prime_number(A[i])

print(sum(answer))


# 숫자의 크기가 크지 않으므로 에라토스테네스의 체를 사용하지 않아도 된다.
