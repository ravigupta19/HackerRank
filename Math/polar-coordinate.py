import cmath
cm = list(input().split())
print(cm[1][:-1])
print('{0:.3}'.format(cmath.phase(complex(float(cm[0]), float(cm[1][:-1])))))
print('{0:.3}'.format(abs(complex(float(cm[0]), float(cm[1][:-1])))))
