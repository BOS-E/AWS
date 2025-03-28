def transpose_matrix(matrix):
    x = len(matrix)
    y = len(matrix[0])

    for i in range(x):
        for j in range(y):
            if i<j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for j in range(y):    
            print(matrix[i][j], end=' ')
        print()
    return matrix

# matrix = [[11,22,33],
#           [44,55,66],
#           [77,88,99]]

# function(matrix)