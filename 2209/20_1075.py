N = str(input())
F = int(input())
L = list(N)
L[-1] = '0'
L[-2] = '0'
N = ''.join(L)
cnt = 0

for i in range(99):
    if (int(N)%F) == 0:
        break
    else:
       N =  int(N) + 1
N = str(N)
print(N[-2::])
