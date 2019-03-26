#This problem is actually to test the platform, but I'll upload it anyway
#i actually had a bit of trouble the first time I was using the platform.

def solveMeFirst(a,b):
    '''This function takes two inputs, that must be numbers, as its arguments.
     It then returns another number, which is the sum of the arguments.'''
    return a + b

#Here's where testng begins
num1 = int(input())
num2 = int(input())
res = solveMeFirst(num1,num2)
print(res)
