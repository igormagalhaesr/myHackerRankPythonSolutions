def timeConversion(s):
    '''This function receives a string with an hour format of 07:05:45PM,
    it then returns the following format 19:05:45'''
    if s[:2] == "12" and s[(len(s) - 2):len(s)] == "PM":
        out = "12" + s[2:(len(s) - 2)]
    
    elif s[(len(s) - 2):len(s)] == "PM":
        out = str(int(s[0:2]) + 12) + s[2:(len(s) - 2)]

    elif s[:2] == "12" and s[(len(s) - 2):len(s)] == "AM":
        out = "00" + s[2:(len(s) - 2)]
    
    else:
        out = s[:(len(s) - 2)]

    return out
