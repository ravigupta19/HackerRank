_, s = input(),set(map(int,input().split()))
for _ in range(int(input())):
    method = input().split()
    getattr(s,method[0])(set(map(int,input().split())))
print(sum(s))