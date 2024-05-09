from numpy import linalg, sort, array, argsort, matmul, allclose
import sys


def match_eigenvectors(matrix):
    try:
        values, vectors = linalg.eig(matrix)
        value_list = []
        vector_list = []
        for value in values:
            for vector in vectors:
                if allclose(matmul(matrix, vector), value * vector):
                    value_list.append(value)
                    vector_list.append(vector)
        sorted_values = array(value_list)
        sorted_vectors = array(vector_list)
    except IndexError:
        print("Please enter square matrix")
    return sorted_values, sorted_vectors


def calculate_lowest_eigenvectors(square_matrix, number_of_eigenvectors=3):
    try:
        matrix_dimension = square_matrix.shape
        if matrix_dimension[0] != matrix_dimension[1]:
            raise IndexError
        elif number_of_eigenvectors > matrix_dimension[0]:
            raise IndexError
        else:
            matched_values, matched_vectors = match_eigenvectors(square_matrix)
            sort_argument = argsort(matched_values)
            eigenvalues = (matched_values[sort_argument])[:number_of_eigenvectors]
            eigenvectors = (matched_vectors[sort_argument])[:number_of_eigenvectors]
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
