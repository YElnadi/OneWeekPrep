'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''
def miniMaxSum(arr):
    # Write your code here
    min_sum = 0
    max_sum = 0
    sorted_arr = sorted(arr)
    
    for num in range(len(sorted_arr)-1):
        min_sum += sorted_arr[num]
    
    for num in range(1, len(sorted_arr)):
        max_sum += sorted_arr[num]
    
    print(min_sum, max_sum)
        