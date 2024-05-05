import numpy
import sys


def read_two_columns_text(filename):
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
