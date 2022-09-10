while True:
    S, A, W = input().split()
    if (S =='#') & (A =='0') & (W == '0'):
        break
    if (int(A) > 17) | (int(W) >=80):
        print(S,'Senior')
    else:
        print(S,'Junior')
