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
        