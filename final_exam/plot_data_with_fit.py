import matplotlib.pyplot as plt
from numpy import linspace
import sys


def plot_data_with_fit(data, fit_curve, data_format='o', fit_format=""):
    try:
        data_x_values = data[0]
        data_y_values = data[1]
        curve_x_values = fit_curve[0]
        curve_y_values = fit_curve[1]
        combined_plot = plt.plot(data_x_values, data_y_values, data_format, curve_x_values, curve_y_values, fit_format)
    except IndexError:
        print("Please make sure data and fit_curve inputs are 2xM dimensional arrays")
        sys.exit(1)
    return combined_plot


if __name__ == "__main__":
    test_data = [[-2, -1, 0, 1, 2], [4, 1, 0, 1, 4]]
    test_fit_curve = [linspace(-2, 2), linspace(-2,2)**2]
    plot_data_with_fit(test_data, test_fit_curve, data_format="x",  fit_format="--")
    plt.show()
