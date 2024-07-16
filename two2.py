# Given a list of non-negative integers, return a list of those numbers multiplied by 2, omitting any of the resulting numbers that end in 2.

# two2([1, 2, 3]) → [4, 6]
# two2([2, 6, 11]) → [4]
# two2([0]) → [0]

def two2(nums):
     #[1,2,3] -> 1x2 = 2(omitted because it ends with 2 - 02 ) 2x2= 4 3x2=6. 
    #[2,6,11] -> 4, 12(omitted), 22(omitted)
    arr = []

    # for i in nums:
    #     res = i * 2
    #     if str(res) != '2' and not str(res).endswith('2'):
    #         arr.append(res)
    # return arr

    for i in nums:
        res = i * 2
        if res % 10 != 2:
            arr.append(res)

    return arr


print(two2([1, 2, 3])) 
print(two2([2, 6, 11]))
print(two2([0]))
