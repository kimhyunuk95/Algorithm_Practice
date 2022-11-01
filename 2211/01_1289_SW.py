T = int(input())

for test_case in range(1, T+1):
    memory = input()
    n = '0'
    cnt = 0

    for i in range(len(memory)):
        if memory[i] != n:
            n = memory[i]
            cnt += 1

    print(f'#{test_case}', cnt)
