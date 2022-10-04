while True:
    n = str(input())
    if n == '0':
        break
    elif n != n[::-1]:
        print('no')
    else:        
        print('yes')

        
 # 복잡하게 생각하지 말고 문자열 슬라이싱으로 풀면 된다.
