N, M = map(int,input().split())
my_dict = {}
my_list = []
for _ in range(N):
    key, val = input().split()
    my_dict[key] = val

for i in range(M):
    item = input()
    my_list.append(item)

for j in range(M):
    print(my_dict[my_list[j]])
    
    
# key-value store인 딕셔너리로 해결하면 간단한 문제이다.
