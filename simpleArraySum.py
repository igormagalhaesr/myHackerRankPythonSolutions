#Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.
#simpleArraySum has the following parameter(s): ar (an array of integers)
#Input Format:
#The first line contains an integer, denoting the size of the array. 
#The second line contains  space-separated integers representing the array's elements.

def simpleArraySum(ar):
    '''this function takes an array as it's argument,
    then it returns the sum of all of the array's elements'''
    
    #I'll simply sum all of the array's elements, from 0, to len(ar) (not inclusive) to the "out" variable and return it
    out = 0
    for i in range(len(ar)):
        out += ar[i]

    return out
