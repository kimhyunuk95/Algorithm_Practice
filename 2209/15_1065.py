x= int(input())
count = 0
answer = 0
if x < 100:
    answer = x
if x >= 100:
    answer = 99
    for i in range(100, x+1):
        if int((i/100)) - int((i/10)%10) == int((i/10)%10) - int(i%10):
            answer += 1

print(answer)

# 두자릿수 까지는 무조건 한수 이다.
# 다 풀어놓고 100에 대한 처리를 해주지 않아 제출을 여러번했다. 꼼꼼하게 확인할 것
