A = int(input())
B = int(input())
C = int(input())

result = A * B * C
answer = [0] * 10
for s in str(result):
    answer[int(s)] = answer[int(s)] + 1
for i in range(10):
    print(answer[i])
