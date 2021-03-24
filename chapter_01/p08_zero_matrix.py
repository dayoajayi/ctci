'''
 Write an algorithm such that if an element in an MxN matrix is 0, its entire row
 and column are set to 0.

 SOLUTION: 

 This solution makes two passes through the matrix - setting the corresponding row and column of each
 0 to None, and the second pass is setting all the encountered None to zero. This prevents double-counting
 of the zeroes on the first pass.
'''

def zero_out_matrix(matrix):
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                set_none(matrix, i, j)
            
    for i in range (len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == None:
                matrix[i][j] = 0
    return matrix

def set_none(matrix, r, c):
    # set the row to None
    for i in range (len(matrix[r])):
        if matrix[r][i] != 0:
            matrix[r][i] = None

    #set the column to None
    for i in range(len(matrix)):
        if matrix[i][c] != 0:
            matrix[i][c] = None
    
    matrix[r][c] = None

matrix = [
    [1,2,3,4],
    [5,0,7,8],
    [6,1,1,2],
    [2,3,4,0]
]

print (zero_out_matrix(matrix))