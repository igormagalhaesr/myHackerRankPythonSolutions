#they give you an array and expect you to sum all the numbers

def aVeryBigSum(ar):
    '''Input is an array.
    The function returns the sum of all it's elements'''
    out = 0
    for i in range(len(ar)):
        out += ar[i]

    return out
