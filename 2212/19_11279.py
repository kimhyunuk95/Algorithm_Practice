import sys

n = int(sys.stdin.readline())
arr = [0]
for _ in range(n):
    a = int(sys.stdin.readline())
    if a == 0:
        print(max(arr))
        max_idx = arr.index(max(arr))
        del arr[max_idx]
    else:
        arr.append(a)

# 단순히 배열을 사용하게 되면 시간 초과가 난다.
# 대략적인 시간 복잡도가 O(n*n)이기 때문

import sys
import heapq

n = int(input())
heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num !=0:
        heapq.heappush(heap,(-num))
        # 구현되어있는 힙큐가 최소힙이므로 음수로 넣어준다.
    else:
        try:
            print(-1 * heapq.heappop(heap))
            # 음수로 넣어주었기 때문에 반전해서 출력해준다.
        except:
            print(0)
