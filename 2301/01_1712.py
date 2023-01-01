a, b, c = map(int,input().split())
if b>=c:
    print(-1)
else:
    print(int(a/(c-b)+1))
    
# b가 c보다 크거나 같으면 손익분기점을 넘을 수 없다.
# 판매가 - 제조비용으로 기초비용을 나눈 후 1을 더해주면 손익분기점을 넘은 시점이게  된다.
