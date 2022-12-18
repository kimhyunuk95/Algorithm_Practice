t = int(input())

for i in range(t):
    dress = dict()
    answer = 1
    n = int(input())
    for j in range(n):
        a, b = input().split()
        if not b in dress:
            dress[b] = 1
        # 해당 옷의 종류가 하나도 없다면 딕셔너리에 추가
        else :
            dress[b] += 1
        # 이미 해당 옷의 종류가 있다면 갯수를 1 증가시켜줌
    for k in dress.keys():
        answer = answer * (dress[k]+1)
    print(answer-1)

# 조합을 이용한 문제 마지막 프린트에서 -1은 옷을 전부 입지 않은 상태를 빼준 것
# 옷의 종류별로 몇개있는지가 중요
