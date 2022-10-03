while True:
    nums = []
    max_num = 0
    min_num = 0
    nums = list(map(int,input().split()))
    max_num = max(nums)
    nums.remove((max_num))
    min_num = min(nums)
    nums.remove((min_num))
    if max_num == min_num == nums[0] == 0:
        break
    if max_num**2 == ((min_num**2) + (nums[0]**2)):
        print('right')
    else :
        print('wrong')
        
        
# 항상 가장 긴변이 마지막에 입력된다고 장담 할 수 없으므로 이렇게 구현하였다.
