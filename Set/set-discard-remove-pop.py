n = int(input())
s = set(map(int, input().split()))
for _ in range(int(input())):
    try:
        method = input().split()
        print(method)
        if len(method) == 1:
            getattr(s, method[0])(*method[1:])
        else:
            getattr(s, method[0])(int(method[1]))
    except KeyError:
        continue
print(sum(s))

