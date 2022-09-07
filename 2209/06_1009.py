import math
T = int(input())

while T:
    a, b = map(int, input().split())
    x_2 = [2, 4, 8, 6]
    x_3 = [3, 9, 7, 1]
    x_4 = [4, 6] 
    x_5 = [5]
    x_6 = [6]
    x_7 = [7, 9, 3, 1]
    x_8 = [8, 4, 2, 6]
    x_9 = [9, 1]
    a = a%10
    if a == 1:
        print(1)
    elif a == 2:
        print(x_2[(b%4)-1])
    elif a == 3:
        print(x_3[(b%4)-1])
    elif a == 4:
        print(x_4[(b%2)-1])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        print(x_7[(b%4)-1])
    elif a == 8:
        print(x_8[(b%4)-1])
    elif a == 9:
        print(x_9[(b%2)-1])
    elif a == 0:
        print(10)
    T -= 1
    
    # 단순히 제곱을 계산하면 큰수가 입력되었을때 시간 초과가 일어난다.
    # 필요한 것은 1의 자리수이므로 반복되는 구간을 찾아 계산한다.
