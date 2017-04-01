#In Python, a string can be split on a delimiter.

def split_and_join(line):
    # writ your code here
     a = line.split(" ")
     return "-".join(a)

print(split_and_join('this is a string'))