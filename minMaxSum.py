def miniMaxSum(arr):
    '''This function takes an array of a len n as its argument
    It, then, prints the minimum and the maximum ossible sum of n-1 of this array's elements'''
    sortedArray = sorted(arr)
    maxSum = sum(arr) - sortedArray[0]
    minSum = sum(arr) - sortedArray[len(sortedArray) - 1]

    print(minSum, maxSum)
