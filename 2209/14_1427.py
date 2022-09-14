n = []

a = input()
a = str(a)
for i in range(len(a)):
    n.append(a[i])
n.sort(reverse=True)
for i in range(len(n)):
    print(int(n[i]), end='')
    
    
# 숫자를 문자열로 취급하여 각 자릿수별 숫자를 간단하게 저장가능
