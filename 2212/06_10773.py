k = int(input())
arr = list()
for _ in range(k):
    n = int(input())
    if not n: # n == 0 일때 리스트의 가장 마지막 숫자를 제거해준다.
        arr.pop()
    else:
        arr.append(n) # n != 0 일때 리스트에 숫자를 추가해준다.
print(sum(arr))

# 배열을 스택으로 이용하여 문제를 풀이 하였다.
