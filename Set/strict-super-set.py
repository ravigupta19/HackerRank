a = set(map(int,input().split()))
superset = True
for _ in range(int(input())):
    b = set(map(int,input().split()))
    if a.issuperset(b):
        if len(a.difference(b)) > 0:
            continue
        else:
            superset = False
            break
    else:
        superset = False
        break
print(superset)
