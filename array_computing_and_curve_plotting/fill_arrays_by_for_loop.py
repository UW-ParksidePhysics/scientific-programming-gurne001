from numpy import array
from fill_gaussian_lists import gaussian

positions = []
gaussian_values = []
for i in range(0, 41):
  positions.append(-4+(8/40)*i)
for i in range(len(positions)):
  gaussian_values.append(gaussian(positions[i]))

x_values = array(positions)
y_values = array(gaussian_values)

print(x_values)
print(y_values)