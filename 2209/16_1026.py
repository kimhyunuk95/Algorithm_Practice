N = int(input())
A, B = list(map(int, input().split())), list(map(int,input().split())) 

A.sort()
B.sort(reverse=True)
S = 0
for i in range(N):
    S += A[i] * B[i]

print(S)

# A를 재배열 할 수 있기 때문에 B를 재배열 하지 못한다는 조건은 의미가 없다.
# 따라서 A를 오름차순, B를 내림차순으로 정렬해 곱했을때 가장 작은 값을 가지도록 해준다.
