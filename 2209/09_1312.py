A, B, N = map(int,input().split())
answer = []
for i in range(N):
    A = A - (B*(A//B))
    A *= 10
answer.append(A%B)
print(A//B)


# N이 1,000,000 까지 이므로 일반적인 자료형으로는 다 담을 수가 없다.
# 따라서 나눗셈을 구현한다는 생각으로 풀이했다.
