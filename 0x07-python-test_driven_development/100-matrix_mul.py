#!/usr/bin/python3

"""
Defines a function that multiplies two matrices.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (matrix): The first matrix.
        m_b (matrix): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list.
        TypeError: If m_a or m_b is not a list of lists.
        TypeError: If any element of those matrix is not an integer or a float.
        ValueError: If m_a or m_b is empty.
        TypeError: If m_a or m_b is not a rectangle
                    (all rows should be of the same size).
        ValueError: If m_a and m_b cannot be multiplied.

    Returns:
        matrix: The product of the two matrices.
    """
    # Error messages
    list_err = "{} must be a list of lists"
    empty_err = "{} can't be empty"
    type_err = "{} should contain only integers or floats"
    size_err = "each row of {} must be of the same size"
    value_err = "{} and {} can't be multiplied"

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        var_name = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError(f"{var_name} must be a list")

    # Check if m_a and m_b are lists of lists
    for matrix in [m_a, m_b]:
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(list_err.format(matrix))

    # Check if m_a and m_b are not empty matrices
    for matrix, name in zip([m_a, m_b], ["m_a", "m_b"]):
        if not matrix or all(not row for row in matrix):
            raise ValueError(empty_err.format(name))

    # Check if all elements in m_a and m_b are integers or floats
    for matrix, name in zip([m_a, m_b], ["m_a", "m_b"]):
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(type_err.format(name))

    # Check if all rows in m_a and m_b have the same size
    row_lengths = set(len(row) for matrix in [m_a, m_b] for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError(size_err.format(
            "m_a" if len(m_a[0]) == min(row_lengths) else "m_b"))

    # Check if the number of m_a columns is equal to the number of m_b rows
    if len(m_a[0]) != len(m_b):
        raise ValueError(value_err.format("m_a", "m_b"))

    # Perform matrix multiplication
    result_matrix = [
            [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
            for row_a in m_a]

    return result_matrix
