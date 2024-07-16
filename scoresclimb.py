# Given an array of scores sorted in increasing order, return true if the array contains 3 adjacent scores that differ from each other by at most 2, such as with [3, 4, 5] or [3, 5, 5]

# scoresClump([3, 4, 5]) → true
# scoresClump([3, 4, 6]) → false
# scoresClump([1, 3, 5, 5]) → true


def scoresClump(scores):
    #[3,4,5] group1 = 5 -3 = 2 return True
    #[3,4,6] group1 = 6 - 3 = 3 return false (should be <= 2)
    #[1,3,5,5] group1 = [1,3,5] -> 5 -1 = 4 group2 = [3,5,5] -> 5-3 = 2 return true
    
    for i in range(len(scores) - 2):
        if scores[i+2] - scores[i] <= 2:
            return True
    return False



print(scoresClump([3, 4, 5])) #→ true
print(scoresClump([3, 4, 6])) #→ false
print(scoresClump([1, 3, 5, 5])) #→ true

