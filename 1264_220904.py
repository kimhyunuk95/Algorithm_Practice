while True:
    n = input()
    if n == '#':
        break
    n = n.lower()
    count = 0
    for s in n:
        if s in ['a','e','i','o','u']:
            count += 1
    print(count)
