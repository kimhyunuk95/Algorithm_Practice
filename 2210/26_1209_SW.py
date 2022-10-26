T = 10

for test_case in range(1, T+1):
    num = int(input())
    nums = [list(map(int,input().split())) for _ in range(100)]
    crs_sum = 0
    crs2_sum = 0
    temp_row = 0
    temp_col = 0
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += nums[i][j]
            if temp_row < row_sum:
                temp_row = row_sum
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += nums[j][i]
            if temp_col < col_sum:
                temp_col = col_sum
    for i in range(100):
        for j in range(100):
            if i == j:
                crs_sum += nums[i][j]
    for i in range(100):
        for j in range(99,0,-1):
            if j == (99-i):
                crs2_sum += nums[i][j]
    print(f'#{test_case}',max(temp_row,temp_col,crs_sum,crs2_sum))
