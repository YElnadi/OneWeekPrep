'''
Given an array of integers, where all elements but one occur twice, find the unique element.
example: a = [1,2,3,4,3,2,1]
answer is 4
'''
def lonelyinteger(a):
    dict_arr = {}
    for num in a:
        if num not in dict_arr:
            dict_arr[num] = 1
        else:
            dict_arr[num] += 1
    # return dict_arr

    for key, value in dict_arr.items():
        if value == 1:
            return key

print(lonelyinteger([1,2,3,4,3,2,1]))