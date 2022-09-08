from collections import OrderedDict
T = int(input())
array = []
while T:
    N = input()
    array.append(N)
    T -= 1
array.sort()
array.sort(key=lambda x : len(x))
array = ' '.join(OrderedDict.fromkeys(array))
array = array.split()
for s in array:
    print(s)
    
    
    
    
# python 3.6 이상부터는 dictionary가 순서유지를 보장하기 때문에 그냥 dictionary를 사용해도 상관없다.
# python에서 문자가 들어가있는 배열을 sort하게 되면 알파벳 순서대로 정렬하므로
# 길이순으로 정렬하는 작업은 lambda를 이용해 따로 해 주었다.
