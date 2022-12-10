t = int(input())

for t in range(t):
    n = int(input())
    d = [0]*101
    d[1] = 1 # 1부터 시작하므로 dp배열에 1부터 넣어주면 편하게 풀이가 가능하다.
    d[2] = 1
    d[3] = 1
    for i in range(4,n+1):
        d[i] = d[i-2] + d[i-3] # 점화식을 알아냈으므로 dp를 사용해준다.
    print(d[n]) 
