#A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
from collections import Counter

number_of_shoes = 10
list_of_size = '2 3 4 5 6 8 7 6 5 18'.split()
dict_of_size = dict(Counter(list_of_size))
total_money_earned = 0
number_of_purchase = int('6')
for i in range(number_of_purchase):
    str_puchase_input = input()
    l = str_puchase_input.split()
    size, prize = l[0], l[1]
    try:
        if dict_of_size[size] == 0:
            raise KeyError
        else:
            dict_of_size[size] = dict_of_size[size] - 1
    except KeyError:
        print('Size no longer available, so no purchase ')
        continue
    else:
        print('Customer {0}: Purchased size {1} shoe for ${2}'.format(i+1, size, prize))
        total_money_earned += int(prize)

print('total earning of shoe marker {0}'.format(total_money_earned))



