#!/usr/bin/python3
"""
Defines a matrix multiplication function.

Attributes:
    m_a (matrix)
    m_b (matrix)
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    # Error messages
    list_error = "{} must be a list of lists"
    empty_error = "{} can't be empty"
    type_error = "{} should contain only integers or floats"
    size_error = "each row of {} must be of the same size"
    value_error = "{} and {} can't be multiplied"

    # Check if m_a and m_b are lists
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        var_name = "m_a" if not isinstance(m_a, list) else "m_b"
        raise TypeError(f"{var_name} must be a list")

    # Check if m_a and m_b are lists of lists
    for matrix in [m_a, m_b]:
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(list_error.format(matrix))

    # Check if m_a and m_b are not empty matrices
    for matrix, name in zip([m_a, m_b], ["m_a", "m_b"]):
        if not matrix or all(not row for row in matrix):
            raise ValueError(empty_error.format(name))

    # Check if all elements in m_a and m_b are integers or floats
    for matrix, name in zip([m_a, m_b], ["m_a", "m_b"]):
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError(type_error.format(name))

    # Check if all rows in m_a and m_b have the same size
    row_lengths = set(len(row) for matrix in [m_a, m_b] for row in matrix)
    if len(row_lengths) > 1:
        raise TypeError(size_error.format(
            "m_a" if len(m_a[0]) == min(row_lengths) else "m_b"))

    # Check if the number of m_a columns equal to the number of m_b rows
    if len(m_a[0]) != len(m_b):
        raise ValueError(value_error.format("m_a", "m_b"))

    # Perform matrix multiplication
    result_matrix = [
            [sum(a * b for a, b in zip(row_a, col_b)) for col_b in zip(*m_b)]
            for row_a in m_a]

    return result_matrix
