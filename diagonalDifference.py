#This problem gives you a diagonal matrix and asks you to compute the difference of the main and secondary diagonals.

def diagonalDifference(arr):
    '''This function takes a matrix as its input.
    It, then, returns the difference of the main and secondary diagonals.'''
    leftToRight = 0
    rightToLeft = 0

    for i in range(len(arr)): #this part is to go through all rows
        for j in range(len(arr)): #then each element in a row, which is a column
            if i == j:
                leftToRight += arr[i][j]
            if i + j == len(arr) - 1:
                rightToLeft += arr[i][j]

    return abs(leftToRight - rightToLeft)
