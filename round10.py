# Write a function to round an int value up to the next multiple of 10 if its rightmost digit is 5 or more. 
# So 15 rounds up to 20, and 6 rounds up to 10. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. 
# Given 3 ints, a b c, return the sum of their rounded values.

# round_sum(16, 17, 18) → 60
# round_sum(12, 13, 14) → 30
# round_sum(6, 4, 4) → 10

import math

def round_sum(a,b,c):
    rounded_sum = 0
    for num in [a,b,c]:
        if num % 10 >=5:
            rounded = math.ceil(num/10) * 10
            rounded_sum += rounded
        else:
            rounded = math.floor(num/10) * 10
            rounded_sum += rounded

    return rounded_sum




print(round_sum(16, 17, 18)) #→ 60
print(round_sum(12, 13, 14)) #→ 30
print(round_sum(6, 4, 4)) #→ 10