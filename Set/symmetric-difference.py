number_ele_s1 = int(input())
s1 = set(map(int,input().split()))
number_ele_s2 = int(input())
s2 = set(map(int,input().split()))
diff = s1.symmetric_difference(s2)
for i in sorted(diff):
    print (i)