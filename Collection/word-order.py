from collections import OrderedDict
N = int(input())
dict_string = OrderedDict()
for i in range(N):
    string = input()
    if string in dict_string:
        dict_string[string] = dict_string[string] + 1
    else:
        dict_string[string] = 1
print(len(dict_string))
print(" ".join(str(values) for values in dict_string.values()))