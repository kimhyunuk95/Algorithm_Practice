for i in range(n):
    a, b = map(int,input().split())
    meet.append([a,b])

meet.sort(key = lambda x:(x[1],x[0]))
# 회의가 끝나는 시간이 빠른순으로(x[1]) 정렬한다.
answer = 0
end = 0

for i in range(len(meet)):
    if end <= meet[i][0]:
        end = meet[i][1]
        answer += 1
#회의가 끝난 시간보다 시작 시간이 크다면 answer += 1
#회의가 끝난 시간을 해당하는 회의의 끝난 시간으로 바꾸어 준다.
print(answer)


# 1.회의가 끝나는 시간이 빠를수록 더 많은 회의를 고를 수 있다.
# 2. 끝난 시간 이후부터 가장 빨리 시작되는 회의를 골라야 한다.
