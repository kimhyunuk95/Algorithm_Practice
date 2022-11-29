x, y = map(int,input().split())

b = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if x == 1:
    month = y
else :
    month = sum(b[:x-1]) + y

num_day = month%7
if num_day == 0:
    print('SUN')
elif num_day == 1:
    print('MON')
elif num_day == 2:
    print('TUE')
elif num_day == 3:
    print('WED')
elif num_day == 4:
    print('THU')
elif num_day == 5:
    print('FRI')
elif num_day == 6:
    print('SAT')
