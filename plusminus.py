'''
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  6 places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
'''

def plusMinus(arr):
    # Write your code here
    arr_len = len(arr)
    pos = 0
    neg = 0
    zero = 0
    for ele in arr:
        if ele < 0:
            neg += 1
        if ele > 0:
            pos += 1
        if ele == 0:
            zero += 1
    print("{0:.6f}".format(pos/arr_len))  
    print("{0:.6f}".format(neg/arr_len))   
    print("{0:.6f}".format(zero/arr_len))     