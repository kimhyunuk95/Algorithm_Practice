n = int(input())
a = set(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

for i in b:
    if i in a:
        print(1)
    else:
        print(0)



# 처음엔 이분탐색으로 문제를 풀려했으나 계속해서 시간 초과가 나와서 찾아본 결과 더 간단한 방법이 있었다.
# python에서 시간복잡도가 list의 search는 O(N)이고 set의 search는 O(1)이다.
# 참고 : https://enjoyso.tistory.com/71

# ↓ 이분 탐색을 시도한 코드
# def find(N, M):
#     M.sort()
#     start = 0
#     end = len(M) -1

#     while start <= end:
#         mid = (start+end) // 2
#         if M[mid] == N:
#             return 1
#         elif M[mid] < N:
#             start = mid + 1
#         else:
#             end = mid - 1
#     return 0


# N = int(input())
# A = list(map(int,input().split()))
# M = int(input())
# B = list(map(int,input().split()))
# for i in B:
#     idx = find(i,A)
#     print(idx)
