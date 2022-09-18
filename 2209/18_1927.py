import heapq
import sys

heap = []

N = int(input())

while N:
    x = int(sys.stdin.readline())
    if not heap:
        if x == 0:
            print(0)
    elif x == 0:
        result = heapq.heappop(heap)
        print(result)
    if x != 0:
        heapq.heappush(heap, x)
    N -= 1
    
    
# heap을 사용하지 않고 하게 되면 시간 초과가 일어난다. 아래있는 코드는 heap을 사용하지 않고 그냥 짜본 코드.
# 9번째 줄에서 input()을 사용하면 시간 초과가 일어나 sys.stdin.realine으로 바꾸어 주었다.

# s_heap = []
# N = int(input())

# while N:
#     x = int(input())
#     if not s_heap:
#         if x == 0:
#             print(0)
#     elif x == 0:
#         print(min(s_heap))
#         s_heap.remove(min(s_heap))
#     if x !=0 :
#         s_heap.append(x)

#     N -= 1
