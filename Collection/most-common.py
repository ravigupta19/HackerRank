from collections import Counter
d_count = dict(Counter(input()))
s = sorted(d_count.items(),key = lambda x:(-x[1],x), reverse = False )
print (s[0][0],s[0][1])
print (s[1][0],s[1][1])
print (s[2][0],s[2][1])