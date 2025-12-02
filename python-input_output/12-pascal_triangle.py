#!/usr/bin/python3
"""Pascal triangle module"""


def pascal_triangle(n):
    """Return a list of lists of integers representing Pascal's triangle of n"""
    if n <= 0:
        return []

    triangle = [[1]]  # ilk sətir

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # hər sətirin ilk elementi 1
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # hər sətirin son elementi 1
        triangle.append(row)

    return triangle
