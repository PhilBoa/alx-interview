#!/usr/bin/python3
""" This module solves the Rotate 2D Matrix problem.
The Rotate 2D Matrix problem involves placing 2D non-attacking on achessboard.
 """
 import sys

def rotate_2d_matrix(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)

