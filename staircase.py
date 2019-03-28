def staircase(n):
    '''This function takes an integer number as its input.
    It then prints a staircase made of #s'''
    for i in range(n):
        print((n - (i + 1))*" " + (i + 1) * "#" )
