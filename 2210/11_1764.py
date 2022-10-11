N, M = map(int,input().split())
no_hear = set()
no_see = set()
cnt = 0

for _ in range(N):
    no_hear.add(input())
for _ in range(M):
    no_see.add(input())
no_hear_see = (no_hear & no_see)
cnt = len(no_hear_see)
no_hear_see = list(no_hear_see)
no_hear_see.sort()
print(cnt)
for i in range(cnt):
    print(no_hear_see[i])




# 처음 짠 코드는 시간 초과가 나왔다.
# 계산을 할때는 순서가 중요하지 않으므로 list보다 빠른 set을 이용해 연산하고 출력할때만 리스트로 바꾸어 해주었다.

# N, M = map(int,input().split())
# no_hear = []
# no_see = []
# no_hear_see = []
# cnt = 0
# for _ in range(N):
#     no_hear.append(input())
# for _ in range(M):
#     no_see.append(input())
# for i in range(N):
#     if no_hear[i] in no_see:
#         cnt += 1
#         no_hear_see.append(no_hear[i])

# no_hear_see.sort()
# print(cnt)
# for i in range(cnt):
#     print(no_hear_see[i])
