n = int(input())
arr = list(map(int,input().split()))
arr = set(arr) # set을 통해 중복을 제거해 준다.
arr = list(arr) # set은 sort를 쓸 수 없고 순서를 보장해 주지 않으므로 다시 list로 형변환해준다.
arr.sort()
for i in range(len(arr)):
    print(arr[i], end=' ')
