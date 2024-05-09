import numpy, matplotlib
from numpy import *
from matplotlib import pyplot
off_diagonal = -1*numpy.ones(4)
upper_diagonal = numpy.diag(off_diagonal, k=1)
lower_diagonal = numpy.diag(off_diagonal, k=-1)
diagonal = numpy.diag((2*numpy.ones(5)))
A = upper_diagonal + lower_diagonal + diagonal

coefficient = 1/(2*((1/6)**2))

H = coefficient*A

eigenvalues, eigenvectors = numpy.linalg.eig(H)
print(eigenvalues)
print(eigenvectors)
x_values = numpy.linspace(1/6, 5/6, 5)


def comparison_function(x):
    f = sqrt(2)*sin(pi*x)
    return f


comparison_x_values = numpy.linspace(0, 1, 50)
comparison_y_values = comparison_function(comparison_x_values)

matplotlib.pyplot.plot(x_values, eigenvectors.T[0])
matplotlib.pyplot.plot(comparison_x_values, comparison_y_values)
matplotlib.pyplot.show()
