def Rev(x):
    x = str(x)
    revX = x[::-1] # 문자열로 바꾸어 뒤부터 기록한다.
    return int(revX) # 덧셈을 계산해야 하므로  int형으로 바꾸어 준다.

x, y = map(int,input().split())
revX = Rev(x)
revY = Rev(y)
print(Rev(revX+revY))
