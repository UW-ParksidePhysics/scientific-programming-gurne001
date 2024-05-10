"""Module defines a function read_two_columns_text that reads a file that is formatted as
two columns of floats/integer values and stores the data"""

__author__ = "Tyler Gurney"

import numpy
import sys


def read_two_columns_text(filename):
    """Takes as input the filename (string) of file to be read, and returns the two
    columns of data in a (2,M) dimensional array called data"""
    data = []
    x_data = []
    y_data = []
    try:
        file = open(filename, 'r')
        for line in file:
            adjusted_line = line.split()
            x_data.append(float(adjusted_line[0]))
            y_data.append(float(adjusted_line[1]))
        data.append(x_data)
        data.append(y_data)
    except OSError:
        print('Cannot find file with that name')
        sys.exit(1)
    data = numpy.array(data)
    return data


if __name__ == "__main__":
    print(f'{read_two_columns_text("volume_energies.dat")}, shape={read_two_columns_text("volume_energies.dat").shape}')
