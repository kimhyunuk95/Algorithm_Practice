n, jimin, hansoo = map(int,input().split())
cnt = 0
while jimin != hansoo:
    jimin -= jimin//2
    hansoo -= hansoo//2
    cnt += 1
print(cnt)

# 토너먼트는 인원수가 라운드가 지날 떄마다 1/2 로 줄어드므로 2로 나눈 몫을 빼주고 라운드는 1씩 올려준다.
