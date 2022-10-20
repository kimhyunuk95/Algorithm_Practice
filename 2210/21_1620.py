import sys

a, b = map(int, sys.stdin.readline().split())
dict_alpha = {}
dict_num = {}
for i in range (1,a+1):
    x = sys.stdin.readline().rstrip()
    dict_alpha[x] = i
    dict_num[i] = x
for i in range (b):
    k = sys.stdin.readline().rstrip()
    if k.isalpha():
        print (dict_alpha[k])
    else:
        print (dict_num[int(k)])
        
# 20일 현재 백준사이트에서 채점이 되지 않는다. 나중에 확인 해 볼것.
