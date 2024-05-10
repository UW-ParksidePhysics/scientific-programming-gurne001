"""Module that defines a function, calculate_bivariate_statistics that calculates statistical values
for a set of 2 dimensional data"""

__author__ = "Tyler Gurney"

from scipy import stats
from read_two_columns_text import read_two_columns_text
from numpy import sqrt, array, linspace
import sys


def calculate_bivariate_statistics(data):
    """Takes a (2,M) dimensional input array of float/int data, and returns a 6 dimensional list
    statistics = [mean_y, stdev_y, min_x, max_x, min_y, max_y]"""
    try:
        statistics_list = []
        stats_array_x = stats.describe(data[0])
        stats_array_y = stats.describe(data[1])
        statistics_list.append(stats_array_y[2])  # mean y
        statistics_list.append(sqrt(stats_array_y[3]))  # stdev y
        statistics_list.append(stats_array_x[1][0])  # min x
        statistics_list.append(stats_array_x[1][1])  # max x
        statistics_list.append(stats_array_y[1][0])  # min y
        statistics_list.append(stats_array_y[1][1])  # max y
        statistics = array(statistics_list)
    except IndexError:
        print('Please make sure input array has shape(2,M)')
        sys.exit(1)
    return statistics


if __name__ == "__main__":
    x_values = linspace(-10,10,21)
    y_values = x_values**2
    test_data = [x_values, y_values]
    print(calculate_bivariate_statistics(test_data))
