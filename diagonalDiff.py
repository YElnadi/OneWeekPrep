'''
Given a square matrix, calculate the absolute difference between the sums of its diagonals.
arr = 1 2 3
      4 5 6
      9 8 9
'''

def diagonalDifference(arr):
    left_to_right = 0
    right_to_left = 0
    n = len(arr)
    for r in range(n):
        left_to_right += arr[r][r]
        right_to_left += arr[r][n - r - 1]

    return abs(left_to_right - right_to_left)
    
    



print(diagonalDifference([[1,2,3],[4,5,6],[7,8,9]]))

