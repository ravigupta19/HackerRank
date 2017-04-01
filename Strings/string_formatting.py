#Given an integer, , print the following values for each integer  from  to :
    #Decimal
    #Octal
    #Hexadecimal (capitalized)
    #Binary
#The four values must be printed on a single line in the order specified above for each  from  to .
#Each value should be space-padded to match the width of the binary value of .
def print_formatted(number):
    pad = len(bin(number)[2:])
    for i in range(1,number+1):
        print('{:>{p}} {:>{p}} {:>{p}} {:>{p}}'.format(i, oct(i)[2:], hex(i).upper()[2:], bin(i)[2:], p = pad))

print_formatted(17)