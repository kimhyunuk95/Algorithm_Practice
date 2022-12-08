n = int(input())
arr = list()
for _ in range(n):
    x, y = map(int,input().split())
    arr.append([y,x]) # sort함수를 쉽게 사용하기 위해 x와 y의 위치를 바꿔서 append시켜준다.
arr.sort()
for x,y in arr:
    print(y,x) # x, y를 뒤집어 append 시켜줬기때문에 다시 뒤집어 출력시켜준다.
