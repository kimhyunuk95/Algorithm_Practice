n = int(input())
score = [0]
total = [0] * 301
for _ in range(n):
    score.append(int(input()))

if n==1:
    total[n] = score[1]
elif n==2:
    total[n] = score[1] + score[2]
else:
    total[1] = score[1]
    total[2] = score[1] + score[2]
    total[3] = max(score[1]+score[3], score[2]+score[3])
    for i in range(4, n+1):
        total[i] = max(total[i-3]+score[i-1]+score[i], total[i-2]+score[i])

print(total[n])

# 다이나믹프로그래밍
