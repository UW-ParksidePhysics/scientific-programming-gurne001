from math import (sin, pi)
from tabulate import tabulate

def sinusoidal_sum(time, number_of_functions, period):
  """Calculates S(t,n), approximation of piecewise functions as defined in assignment"""
  sum = 0
  for i in range(1, number_of_functions + 1):
    sum += (1/((2*i)-1)) * sin(((4*i-2)*pi*time)/period)
    i += 1
  return (4/pi)*sum

def piecewise_function(time, period):
  """Calculates the value of the piecewise function as defined in assignment at time t"""
  if time == 0:
    return period/2
  elif 0 < time < period/2:
    return 1
  elif period/2 < time < period:
    return -1
  else:
    print("Error: Need 0 < t < period")

n_list = [1, 3, 5, 10, 30, 100]
alpha_list = [0.01, 0.25, 0.49]
period = 2*pi
time_list = []
for a in alpha_list:
  time_list.append(period*a)

table = []
for i in range(len(n_list)):
  row_i = []
  for j in range(len(alpha_list)):
    row_i.append(piecewise_function(time_list[j], period) - sinusoidal_sum(time_list[j], n_list[i], period))
    j += 1
  table.append(row_i)
  row_i.insert(0, n_list[i])
  i += 1

print("The error in approximation between S(t,n) and f(t) related to the corresponding values of n and t:")


header_list = ['n', '.01T', ".025T", ".049T"]


print(tabulate(table, headers=header_list, tablefmt="fancy_grid"))