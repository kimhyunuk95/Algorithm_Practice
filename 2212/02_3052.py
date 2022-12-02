n = list()
for _ in range(10):
    n.append(int(input())) # 수 10개를 입력받아 배열에 저장
arr = list()
for i in range(10):
    arr.append(n[i] %42) # 42로 나눈 나머지를 저장
arr = set(arr) # set을 통해 중복된 숫자를 제거해줌
print(len(arr)) # set의 길이가 곧 중복되지 않은 숫자의 갯수
