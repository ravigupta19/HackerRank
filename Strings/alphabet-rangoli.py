#You are given an integer,N .
# Your task is to print an alphabet rangoli of size .
#(Rangoli is a form of Indian folk art based on creation of patterns.)
#Different sizes of alphabet rangoli are shown below:
#size 3

#----c----
#--c-b-c--
#c-b-a-b-c
#--c-b-c--
#----c----

#size 5

#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

#My version of code
from string import ascii_lowercase
def print_rangoli(size):
    pad = size * 4 - 3
    string_alphabet = ascii_lowercase[:size]

    #upper part of rangaloi
    for i in range(1,size):
        string = string_alphabet[-i:]

        if len(string) > 1:
            prefix_string = string[1:][::-1]
            entire_string = prefix_string + string
            list_letter = [letter for letter in entire_string]
            string = ("-").join(list_letter)
            print(string.center(pad,'-'))
        else:
            print(string.center(pad,'-'))

    #middle belt
    prefix_string = string_alphabet[1:][::-1]
    entire_string = prefix_string + string_alphabet
    list_letter= [letter for letter in entire_string]
    print(("-").join(list_letter))

    #lower belt

    for i in range (size-1,0,-1):
        string = string_alphabet[-i:]
        if len(string) > 1:
            prefix_string = string[1:][::-1]
            entire_string = prefix_string + string
            list_letter = [letter for letter in entire_string]
            string = ("-").join(list_letter)
            print(string.center(pad, '-'))
        else:
            print(string.center(pad,'-'))



print_rangoli(10)


#Improved version of Code
def print_rangoli(size):

    Fill_char = '-'  # constant filler character.
    line_width = size*4-3  # width of a line in this size of rangoli.
    reversed_chars = string.ascii_lowercase[0:size][::-1]  # characters used, in reverse order.

    def palindromed(s):
        """ e.g. turns 'abc' into 'abcba' """
        return s[:len(s)-1]+s[::-1]

    lines_of_chars = palindromed([palindromed(reversed_chars[:i+1]) for i in range(size)])

    for line_chars in lines_of_chars:
        print(Fill_char.join(line_chars).center(line_width, Fill_char))

