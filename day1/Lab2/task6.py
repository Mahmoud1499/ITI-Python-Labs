def diagonalDifference(arr):

    n = len(arr)
    diagonal1 = 0
    diagonal2 = 0
    for i in range(0, n):
        diagonal1 = diagonal1 + arr[i][i]

    for j in range(0, n):
        diagonal2 = diagonal2 + arr[j][n-1-j]

    return abs(diagonal1 - diagonal2)
