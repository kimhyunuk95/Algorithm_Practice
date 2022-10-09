n = int(input())
p = list(map(int,input().split()))
p.sort()
sum = 0
total = 0
for i in range(len(p)):
    for j in range(i+1):
        sum += p[j]
    total += sum
    sum = 0

print(total)
