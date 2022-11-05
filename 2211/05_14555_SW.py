T = int(input())

for test_case in range(1, T+1):
    field = str(input())
    cnt = 0
    for i in range(len(field)-1):
        if field[i] == '(' and field[i+1] == ')':
            cnt += 1
        elif field[i] == '(' and field[i+1] == '|':
            cnt += 1
        elif field[i] == '|' and field[i+1] == ')':
            cnt += 1
    print(f'#{test_case}', cnt)
