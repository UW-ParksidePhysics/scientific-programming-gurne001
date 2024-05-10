"""Module defines a function that takes a square matrix and returns a list of the
lowest n eigenvectors and their matching eigenvalues"""

__author__ = "Tyler Gurney"

from numpy import linalg, sort, array, argsort, matmul, allclose, ones, diag, linspace
import sys


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    """Takes as input a square matrix (raises error if matrix not square) and an integer representing the number of
    eigenvectors/values to be stored in the list that is returned.
    Returns a list of the lowest K (default K=3) eigenvalues, and their corresponding eigenvectors"""
    try:
        matrix_dimension = square_matrix.shape
        if matrix_dimension[0] != matrix_dimension[1]:
            raise IndexError
        elif number_of_eigenvectors > matrix_dimension[0]:
            raise IndexError
        else:
            values, vectors = linalg.eig(square_matrix)
            sort_argument = argsort(values)
            eigenvalues = (values[sort_argument])[:number_of_eigenvectors]
            eigenvectors = (vectors[:,sort_argument])[:number_of_eigenvectors]
    except IndexError:
        print("Please enter valid square matrix and valid number of eigenvectors to pull from said matrix\n"
              "Note that number_of_eigenvectors cannot exceed the dimension(s) of square_matrix")
        sys.exit(1)
    return eigenvalues, eigenvectors


if __name__ == "__main__":
    test_square_matrix = array([[2, -1], [-1, 2]])
    print(f'{test_square_matrix.shape}')
    test_number_of_eigenvalues = 2
    print(calculate_lowest_eigenvectors(test_square_matrix, test_number_of_eigenvalues))