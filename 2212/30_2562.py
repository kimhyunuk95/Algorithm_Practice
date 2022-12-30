arr = [int(input()) for _ in range(9)]
print(max(arr))
print(arr.index(max(arr))+1)

# index는 0부터 시작하기 때문에 1을 더해준다.
