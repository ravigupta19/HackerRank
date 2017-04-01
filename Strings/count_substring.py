#Count no of the substring


def count_substring(string, sub_string):
    count = 0
    length_sub_string = len(sub_string)
    for i in range(len(string)):
        if sub_string == string[i:i+length_sub_string]:
            count += 1
    return count

print(count_substring('ABCDCDC','CDC'))