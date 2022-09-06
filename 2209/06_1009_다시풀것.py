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
        print(x_2[((b%10)%len(x_2))-1])
    elif a == 3:
        print(x_3[((b%10)%len(x_3))-1])
    elif a == 4:
        print(x_4[((b%10)%len(x_4))-1])
    elif a == 5:
        print(5)
    elif a == 6:
        print(6)
    elif a == 7:
        print(x_7[((b%10)%len(x_7))-1])
    elif a == 8:
        print(x_8[((b%10)%len(x_8))-1])
    elif a == 9:
        print(x_9[((b%10)%len(x_9))-1])
    elif a == 0:
        print(10)
    T -= 1
