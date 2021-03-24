'''
 Given an image represented by an NxN matrix, where each pixel in the image is repreesnted by an integer, 
 write a method to rotate the image by 90 degrees. Can you do this in place?

SOLUTION: The easiest way to do this in place is to transpose the matrix then flip the transposed matrix
along the vertical axis

'''

def rotate_matrix(matrix):
    # transpose matrix
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # flip matrix along vertical axis - oppI is the opposing index to i
    for r in range(len(matrix)):
        for i in range(len(matrix[r]) // 2):
            oppI = len(matrix[r]) - 1 - i
            matrix[r][i], matrix[r][oppI] = matrix[r][oppI], matrix[r][i]

    return matrix

matrix = [
          [1,2,3],
          [4,5,6],
          [7,8,9]
         ]

'''
Expected Output: 
[
 [7, 4, 1],
 [8, 5, 2], 
 [9, 6, 3]
]
'''

print(rotate_matrix(matrix))
