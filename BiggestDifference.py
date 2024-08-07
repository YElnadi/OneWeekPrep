# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. 

# biggest_diff([10, 3, 5, 6]) → 7
# biggest_diff([7, 2, 10, 9]) → 8
# biggest_diff([2, 10, 7, 2]) → 8

def biggest_diff(nums):
    min_num = min(nums)
    max_num = max(nums)
    return max_num - min_num


print(biggest_diff([10, 3, 5, 6]))
print(biggest_diff([7, 2, 10, 9]))
print(biggest_diff([2, 10, 7, 2]))