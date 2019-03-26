def plusMinus(arr):
    '''This function takes an array as it's input.
    It then returns:
    A decimal representing of the fraction of positive numbers in the array compared to its size.
    A decimal representing of the fraction of negative numbers in the array compared to its size.
    A decimal representing of the fraction of zeros in the array compared to its size.
    '''

    positives = 0
    negatives = 0
    zeroes = 0
    leng = len(arr)
    for i in range(len(arr)):
        if arr[i] > 0:
            positives += 1
        elif arr[i] < 0:
            negatives += 1
        else:
            zeroes += 1
            
    first = round((positives / leng), 6)
    second = round((negatives / leng), 6)
    third = round((zeroes / leng), 6)
    
    print("{0:.6f}".format(first))
    print("{0:.6f}".format(second))
    print("{0:.6f}".format(third))

