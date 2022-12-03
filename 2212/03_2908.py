a, b = map(str,input().split())

a = int(a[::-1])
b = int(b[::-1]) # 문자열로 입력받아 거꾸로 읽어준 후 숫자로 형변환 한다.

if a > b:
    print(a)
else:
    print(b)
