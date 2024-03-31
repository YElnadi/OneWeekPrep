def findMedian(arr):
    # Write your code here
    sortedArr =sorted(arr)
    print(sortedArr)
    lenArr = len(sortedArr)
    print(lenArr)
    
    pos = (lenArr - 1) // 2
    print(pos)
    median = sortedArr[pos]
    print(median)
    return median