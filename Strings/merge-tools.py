#Merge Tools
from collections import OrderedDict
def merge_the_tools(string, k):
    length = len(string)
    for i in range(0, length, k):
        print("".join(OrderedDict.fromkeys(string[i:i + k])))

merge_the_tools()