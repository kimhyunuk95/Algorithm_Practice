from collections import Counter

s = input()
s = s.upper()
word_count = Counter(s)
if len(s) < 1:
    print('?')
if len(s) == 1:
    print(s)
elif Counter(s).most_common(1)[0][1] == Counter(s).most_common(2)[1][1]:
    print('?')
else :
    print(Counter(s).most_common(1)[0][0])
    
    
    
# collections의 Counter를 이용하여 간단하게 해결함.
# Counter는 딕셔너리 형태로 반환됨
# most_common은 리스트 안의 튜플 형태로 반환됨
