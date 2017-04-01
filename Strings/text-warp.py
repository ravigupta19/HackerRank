#Task

#You are given a string S and width W.
#Your task is to wrap the string into a paragraph of width w.

#Input Format

#The first line contains a string, S.
#The second line contains the width, w.
#Sample Output

    #ABCD
    #EFGH
    #IJKL
    #IMNO
    #QRST
    #UVWX
    #YZ



import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

print(wrap('ABCDEFGHIJKLIMNOQRSTUVWXYZ',4))

