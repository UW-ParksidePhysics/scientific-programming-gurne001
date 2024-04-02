from numpy import linspace, array
from fill_gaussian_lists import gaussian

positions = linspace(-4, 4, 41)
gaussian_values = gaussian(positions)

print(positions)
print(gaussian_values)