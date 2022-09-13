x, y = map(int, input().split())

for i in range(x, y+1):
    if i ==1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i%j ==0:
            break
    else:
        print(i)
        
        
# 일반적인 소수 구하는 방식을 사용하면 시간 초과가 나온다.
# 에라토스테네스의 체를 이용한다.
