def birthdayCakeCandles(ar):
    '''This function receives an array as its argument,
    it then returns the number of occurences of the max element'''
    n = -1
    count = 0
    sortedArray = sorted(ar)

    if sortedArray[0] == sortedArray[-1]:
        count = len(ar)
    
    else:
        while sortedArray[n] == sortedArray[n - 1]:
            count += 1
            n -= 1

        count += 1

    return count
