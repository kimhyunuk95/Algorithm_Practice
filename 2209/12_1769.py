x = int(input())
cnt = 0

def solution(x):
    n = [int(i) for i in str(x)]
    return sum(n)

while x%10 != x:
    x = solution(x)
    cnt += 1
print(cnt)
if x == 3 or x==6 or x==9:
    print('YES')
else:
    print('NO')
    
    
# python3로 제출하면 시간 초과가 나온다 pypy3로 제출할것
# 리스크 컴프리헨션이 for문 보다 빠르다.
