import numpy.polynomial
from numpy import polynomial, linspace
import sys


def calculate_quadratic_fit(data):
    try:
        fit_polynomial = numpy.polynomial.polynomial.polyfit(data[0], data[1], 2)
    except IndexError:
        print("Error with input data, please make sure input data is 2xM array")
        sys.exit(1)
    return fit_polynomial


if __name__ == "__main__":
    print(calculate_quadratic_fit([numpy.linspace(-1, 1), numpy.linspace(-1, 1)**2]))
