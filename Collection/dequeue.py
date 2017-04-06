from collections import deque
d = deque()
N = int(input())
for _ in range(N):
    method = input().split()
    getattr(d,method[0])(*method[1:])
print(" ".join(d))
