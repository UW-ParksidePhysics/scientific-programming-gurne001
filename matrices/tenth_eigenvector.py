import matplotlib.pyplot
import numpy
from numpy import *
from matplotlib import pyplot

matrix_dimension = 10

off_diagonal = -1*numpy.ones((matrix_dimension-1))
upper_diagonal = numpy.diag(off_diagonal, k=1)
lower_diagonal = numpy.diag(off_diagonal, k=-1)
diagonal = numpy.diag(2*numpy.ones(matrix_dimension))
A = upper_diagonal + lower_diagonal + diagonal

coefficient = 1/(2*((1/matrix_dimension)**2))

H = coefficient*A

eigenvalues, eigenvectors = numpy.linalg.eig(H)

x_values = numpy.linspace(1/(matrix_dimension+1), matrix_dimension/(matrix_dimension+1), matrix_dimension)


def comparison_function(x):
    f = sqrt(2)*sin(pi*x)
    return f


comparison_x_values = numpy.linspace(0, 1, 50)
comparison_y_values = comparison_function(comparison_x_values)

matplotlib.pyplot.plot(comparison_x_values, comparison_y_values)
matplotlib.pyplot.plot(x_values, eigenvectors.T[0])  # Include .T for purpose of graphing
matplotlib.pyplot.show()