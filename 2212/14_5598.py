wrd = list(input())
for i in range(len(wrd)):
    tmp = ord(wrd[i]) - 3 
    if tmp < ord('A'):
        tmp += 26
    wrd[i] = chr(tmp)
print(''.join(wrd))

# 아스키코드를 이용해주면 쉽게 풀 수 있다.
# https://ko.wikipedia.org/wiki/ASCII
