def fill_spiral_clockwise(n):
    # Create an empty matrix of size n x n
    matrix = [[0] * n for _ in range(n)]

    # Define boundaries
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1  # Start filling from 1

    while top <= bottom and left <= right:
        # Fill top row
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        # Fill right column
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        # Fill bottom row
        if top <= bottom:
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

        # Fill left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

# Create a 7x7 matrix filled in a spiral order
n = 7
spiral_matrix = fill_spiral_clockwise(n)

# Print the matrix
for row in spiral_matrix:
    print(row)
