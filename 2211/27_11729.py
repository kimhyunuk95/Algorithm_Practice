def hanoi(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6-start-end)
    print(start, end)
    hanoi(n-1, 6-start-end, end)

n = int(input())
print(2**n-1)
hanoi(n, 1, 3)

# 하노이의 탑
# 재귀를 이용해 풀어준다
# 6은 막대의 번호 (1,2,3)을 모두 더해주어 나오는 값이다.
