#this function grades stundents with some rules

def gradingStudents(grades):
    '''This functions receives an array with the student's grades,
    it, then, returns their grades rounded if the rounding rules apply'''
    for i in range(len(grades)):
        if grades[i] >= 38:
            if (grades[i] + 2) % 5 == 0:
                grades[i] = grades[i] + 2
            
            elif (grades[i] + 1) % 5 == 0:
                grades[i] = grades[i] + 1
    
    return grades

