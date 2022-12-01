n = int(input())
for _ in range(n):
    sum = 0
    temp = 1
    oxList = str(input())
    for i in range(len(oxList)):
        if oxList[i] == 'O':
            if i != 0:
                if oxList[i-1] == 'O':
                    temp += 1 # 배열에서 o가 처음이 아니라면 temp의 숫자를 늘려준다.
            sum += temp # 배열에서 o를 만나면 temp를 sum에 더해준다.
        elif oxList[i] == 'X':
            temp = 1 # 배열에서 x를 만나면 temp를 1로 초기화 해준다.
    print(sum)
