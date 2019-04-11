def breakingRecords(score):
    minScore = maxScore = score[0]
    minCount = maxCount = 0

    for i in score[1:]:
        if i > maxScore:
            maxCount += 1
            maxScore = i
        
        if i < minScore:
            minCount += 1
            minScore = i
    
    return maxCount, minCount
