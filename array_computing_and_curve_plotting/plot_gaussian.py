import matplotlib.pyplot as plt
from fill_gaussian_lists import gaussian
from numpy import linspace, array

x_values = linspace(-4, 4, 41)
y_values = gaussian(x_values)

plt.plot(x_values, y_values)