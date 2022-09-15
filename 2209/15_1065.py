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

# 두자릿수까지는 무조건 한수이다.
# 다 풀어놓고 100에 대한 처리를 해주지 않아 여러번 제출하였다. 꼼꼼히 확인 할 것
