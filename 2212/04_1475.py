n = str(input())
cnt = [0] * 10 # 각 숫자가 몇번 나왔는지 기록할 배열을 만듦
for i in range(len(n)):
    num = int(n[i])
    if num == 6 or num == 9: # 6과 9는 뒤집어서 사용 가능
        if cnt[6] <= cnt[9]: 
            cnt[6] += 1 
        else:
            cnt[9] += 1
    else:
        cnt[num] += 1
print(max(cnt))
