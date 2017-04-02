#In this challenge, you will be given  integers, n and m.
# There are n words, which might repeat, in word group A.
# There are m words belonging to word group B. For each m words, check whether the word has appeared in group A or not.
# Print the indices of each occurrence of M in group . If it does not appear, print -1.

from collections import defaultdict
number_of_inputs = '5 2'.split()
dict_for_a = defaultdict(list)
for i in range(1,int(number_of_inputs[0])+1):
    key_input = input()
    dict_for_a[key_input].append(str(i))
for i in range(int(number_of_inputs[1])):
     search_key = input()
     if len(dict_for_a[search_key]) == 0:
         print('-1')
     else:
         print(" ".join((dict_for_a[search_key])))


