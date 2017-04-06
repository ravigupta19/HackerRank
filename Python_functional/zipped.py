m,n = map(int,input().split())
X = []
for i in range(n):
      X += [map(float,input().split())]
zipped = zip(*X)
for i in zipped:
    print('{0:0.1f}'.format(sum(i)/n))
