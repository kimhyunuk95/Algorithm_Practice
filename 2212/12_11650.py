n = int(input())
arr = list()

for _ in range(n):
    x, y = map(int,input().split())
    arr.append([x,y])

arr.sort() # x를 기준으로 정렬
for x, y in arr:
    print(x, y)

# Python3로 제출하면 시간초과가 난다.
# 찾아보니 input()이 느리기 때문이라고 한다.
# 대신 sys모듈을 import하고 sys.stdin.readline()을 사용해주면 해결된다.
