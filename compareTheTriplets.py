#You have two arrays, both of them with the same amount of grades (elements), three of them
#You must compare them 1 by 1, and award a point for alice or bob for each of these comparisons

def compareTriplets(a, b):
    '''This functions has as it's inputs two arrays of length three each.
       The output is an array of length 2, the first element returning Alice's points and the second one returning Bob's'''
    out = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            out[0] += 1
        elif a[i] < b[i]:
            out[1] += 1

    return out
