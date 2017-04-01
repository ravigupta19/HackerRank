#My version of code

def minion_game(string):
    vowels = 'AEIOU'
    constants = 'BCDFGHJKLMNPQRSTVXZ'
    score_stuart = 0
    score_kevin  = 0
    set_sub_constants = set()
    set_sub_vowels = set()
    def count_sub_string(para_string,sub_string):
        count = 0
        length_sub_string = len(sub_string)
        for i in range(len(string)):
            if sub_string == string[i:i + length_sub_string]:
                count += 1
        return count

    for len_sub_string in range(1,len(string)+1):
        for i in range(len(string)):
            sub_string = string[i:i + len_sub_string]
            if sub_string[0] in constants:
                set_sub_constants.add(sub_string)
            else:
                set_sub_vowels.add(sub_string)

    for sub_string in set_sub_constants:
        score_stuart += count_sub_string(string,sub_string)
    for sub_string in set_sub_vowels:
        score_kevin += count_sub_string(string,sub_string)

    if score_kevin > score_stuart:
        print('Kevin '+ str(score_kevin))
    elif score_stuart > score_kevin:
        print('Stuart '+ str(score_stuart))
    else:
        print('Draw')

#Improved version of code
def minion_game(string):
    # your code goes here
    length=len(string)
    stu=0
    kev=0
    for i in range(length):
        if string[i] not in ['A','E','I','O','U']:
            stu += length-i
        else:
            kev += length-i
    if stu>kev:
        print("Stuart {}".format(stu))
    elif kev>stu:
        print("Kevin {}".format(kev))
    else:
        print('Draw')

minion_game('BANANA')

