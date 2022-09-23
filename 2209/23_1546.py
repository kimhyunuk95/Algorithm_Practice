N = int(input())
M = list(map(int,input().split()))

M.sort()
for i in range(len(M)):
    M[i] = (M[i]/M[-1])*100

print(sum(M)/len(M))

# 백준 사이트에서는 numpy import가 되지 않는다...코딩테스트 사이트별로 import가능한 라이브러리를 미리 알아보는 것도 좋을 것 같다.
