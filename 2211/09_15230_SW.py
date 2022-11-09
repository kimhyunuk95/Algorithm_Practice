T = int(input())

for test_case in range(1, T+1):
    vocab = str(input())
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    cnt = 0
    for i in range(len(vocab)):
        if alpha[i] == vocab[i]:
            cnt += 1
        elif alpha[i] != vocab[i]:
            break
    print(cnt)
