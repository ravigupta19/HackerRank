from collections import OrderedDict
N = int(input())
dict_of_items = OrderedDict()
for i in range(N):
    str_items = input().split()
    item_name = " ".join(str_items[:-1])
    prize = int(str_items[-1])
    if item_name in dict_of_items:
       dict_of_items[item_name] = dict_of_items[item_name] + prize
    else:
        dict_of_items[item_name] = int(prize)
for item, prize in dict_of_items.items():
    print('{0} {1}'.format(item,prize))