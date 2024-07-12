# Write a function to return the sum of the numbers in the given array 'nums', except ignore sections of numbers starting with a 7 and extending to the next 8 (every 7 will be followed by at least one 8). 
# Return 0 for no numbers.

# sum78([1, 2, 2]) → 5
# sum78([1, 2, 2, 7, 99, 99, 8]) → 5
# sum78([1, 1, 7, 8, 2]) → 4

def sum78(nums):
    sum_sums = 0
    i = 0
    while i< len(nums):
        if nums[i] == 7:
            while i < len(nums) and nums[i] != 8:
                i += 1
            if i<len(nums) and nums[i] == 8:
                i+=1
        else:
            sum_sums += nums[i]
            i += 1
    return sum_sums

print(sum78([1, 2, 2])) 
print(sum78([1, 2, 2, 7, 99, 99, 8])) 
print(sum78([1, 1, 7, 8, 2]))