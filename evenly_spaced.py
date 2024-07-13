# Given three ints, a b c, one of them is small, one is medium and one is large. 
# Return true if the three values are evenly spaced, so the difference between small and medium is the same as the difference between medium and large.

# evenlySpaced(2, 4, 6) → true
# evenlySpaced(4, 6, 2) → true
# evenlySpaced(4, 6, 3) → false

def evenlySpaced(a, b, c):
    sorted_nums = sorted([a,b,c])
    diff1 = sorted_nums[1] - sorted_nums[0]
    diff2 = sorted_nums [2] - sorted_nums[1]
    return diff1 == diff2


print(evenlySpaced(2, 4, 6))
print(evenlySpaced(4, 6, 2))
print(evenlySpaced(4, 6, 3))