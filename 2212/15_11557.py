t = int(input())

for _ in range(t):
    n = int(input())
    univ = dict()
    for _ in range(n):
        a, b = input().split()
        univ[a] = int(b) # 딕셔너리에 대학이름을 key로 술의양을 value로 추가해줌
    print(max(univ,key=univ.get)) # 딕셔너리에서 max value의 key를 출력해준다.

