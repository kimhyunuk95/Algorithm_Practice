n = int(input())
arr = list()
for i in range(n):
    arr.append(int(input()))
arr.sort()
for i in arr:
    print(i)



# 다음과 같이 퀵정렬로도 풀 수 있다.
# 그러나 시간 복잡도가 퀵정렬은 최악의 경우 O(n^2)이다.
# 언어에 내장되어있는 라이브러리는 보통 O(n* log 2 n)이다.

n = int(input())
arr = list()
for i in range(n):
    arr.append(int(input()))
for i in range(n):
    for j in range(i+1, n):
        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
for i in arr:
    print(i)
