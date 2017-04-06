for _ in range(int(input())):
    try:
        l_num = input().split()
        l_num= [int(num)for num in l_num]
        print(l_num[0]//l_num[1])
    except ZeroDivisionError as e:
         print('Error Code: {0}'.format(e))
    except ValueError as e:
        print('Error Code: {0}'.format(e))
