N = int(input())
person = list()
rank = [1 for x in range(N)]
k = 1
for _ in range(N):
    x, y = map(int,input().split())
    person.append([x, y])

for i in range(N):
    for j in range(N):
        if person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            rank[i] += 1
    
for k in range(N):
    print(rank[k], end=' ')
