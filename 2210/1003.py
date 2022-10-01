zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])
    print('{} {}'.format(zero[num], one[num]))

T = int(input())
    
for _ in range(T):
    fibonacci(int(input()))
    
    
# 재귀함수로 풀게되면 시간초과가 일어나게 되어 다이나믹 프로그래밍으로 풀어야 한다.
# fibonacci(n)을 호출했을때 실행되는 fibonacci(0)과 fibonacci(1)은 
# (fibonacci(n-1)의 0과 1 호출횟수) + (fibonacci(n-2)의 0과 1 호출횟수) 와 동일함을 이용한다.
# 참고 : https://itstory1592.tistory.com/34
