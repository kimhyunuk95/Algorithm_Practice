T = int(input())

for test_case in range(1, T+1):
    vocab = str(input())
    vocab = vocab.replace('a','')
    vocab = vocab.replace('i','')
    vocab = vocab.replace('e','')
    vocab = vocab.replace('o','')
    vocab = vocab.replace('u','')
    print(vocab)


#아래처럼 정규표현식이 가능할 줄 알았는데 되지 않았다...

# import re

# T = int(input())

# for test_case in range(1, T+1):
#     vocab = re.compile(r'[aeiou]')
#     ans = vocab.sub('',str(input()))
#     print(f'#{test_case}',ans)
