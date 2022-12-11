n = int(input())

file  = dict()
for i in range(n):
    arr = list(map(str,input().split('.')))# .을 기준으로 구분해준다.
    if not arr[1] in file: # dict에 없으면 추가해고 있으면 value를 1 올려준다.
        file[arr[1]] = 1
    else:
        file[arr[1]] += 1

sort_file = sorted(file.items())

for key, value in sort_file:
    print(key, value)
