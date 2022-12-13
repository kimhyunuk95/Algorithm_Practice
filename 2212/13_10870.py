n = int(input())
d = [0] * 21 # 20이하의 수라고 되어있기때문에 21까지 만들어준다.
d[1] = 1
for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2] # 점화식을 써서 dp을 해준다.
print(d[n])
