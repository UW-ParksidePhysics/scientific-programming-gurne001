"""This program is designed to evaluate the direction/magnitude of electric currents within a simple multiloop circuit.

The program imports sys and numpy; sys is used for exiting functions when errors occur, numpy for matrix calculations and arrays.

The program defines 5 separate functions:

collect_direction_values()
which prompts the user to input the direction of currents in each node, and returns the input as a list. These inputs should specifically be 'in' or 'out'.

collect_voltage_values()
which prompts the user to input the values for the voltages of the circuit's power supplies and returns the input as a list. These inputs should be positive real numbers.

collect_resistance_values()
which prompts the user to input the values for the resistances of the circuit's resistors and returns the input as a list. These inputs should be positive real numbers.

calculate_current_values(direction_values, voltage_values, resistance_values)
which takes lists of a specific dimension as an input and then calculates the current values and directions, returning two arrays with the corresponding values/directions

plot_current_values(current_amps, final_direction_values)
which takes the output lists of calculate_current_values and uses them to plot a representation of the currents around node 1 using their final directions and values"""


import sys
import numpy
import matplotlib.pyplot as plt


def collect_direction_values():
  """Collects the direction of currents in each node from the user. Valid inputs are 'in' or 'out'. Returns a list of the input values for use in later calculations."""

  direction_values = ["?","?","?"]  # Initialize list with placeholder values
  try:
    for i in range(0,3):
      direction_values[i]=str(input(f"Current direction for i{i+1} (in/out): "))  #Prompts user for inputs to replace placeholder values in list
      if direction_values[i] != "in" and direction_values[i] != "out":
        raise ValueError  # Raises error if input is not 'in' or 'out'
  except ValueError:
    print("Invalid input, please enter 'in' or 'out'")
    sys.exit(1)  # Notifies user and kills program if improper input is given
  return direction_values


def collect_voltage_values():
  """Collects the voltage values of the circuit's power supplies from the user. Valid inputs are positive real numbers. Returns a list of the voltage values for use in later calculations"""

  voltage_values = [0., 0.]  # Initialize list with placeholder values
  try:
    for i in range(0,2):
      voltage_values[i]=float(input(f"Voltage for e{i+1} (in volts): "))  # Prompts user for inputs to replace placeholder values in list
      if voltage_values[i]<0:
        raise ValueError  # Raises error for negative numbers
  except ValueError:
    print("Please input a valid number")  # Notifies user and kills program if improper input is given
    sys.exit(1)
  return voltage_values


def collect_resistance_values():
  """Collects the resistance values of the circuit's resistors from the user. Valid inputs are positive real numbers. Returns a list of the resistance values for use in later calculations."""

  resistance_values = [0., 0., 0.]  # Initialize list with placeholder values
  try:
    for i in range(0,3):
      resistance_values[i]=float(input(f"Resistance for R{i+1} (in ohms): "))  # Prompts user for inputs to replace placeholder values in list
      if resistance_values[i]<0:
        raise ValueError  # Raises error for negative numbers
  except ValueError:
    print("Please input a valid number")
    sys.exit(1)  # Notifies user and kills program if improper input is given
  return resistance_values


def calculate_current_values(direction_values, voltage_values, resistance_values):
  """Takes lists of direction, voltage, and resistance values (of specific dimension(s)) as input, and returns two arrays with the corresponding current values and directions.

  The function first calculates the constant matrix A for eqn Ax=b, where A is determined as the product of a matrix R and a matrix D, where R is the matrix of resistance values (w/ placeholders for multiplication in final row) and D represents the effects of the users chosen current directions on the signs of the values in the equation.

  The function then solves the matrix equation Ax=b via numpy's linalg.solve function, and performs additional calculations to determine the correct direction of the currents based on the signs of the values in vector x.

  The function then returns two arrays, one with the proper current directions and another with the magnitude of the currents."""
  try:
    R = numpy.array([[resistance_values[0], 0, resistance_values[2]],
                   [0, resistance_values[1], resistance_values[2]],
                   [1, 1, 1]])  # R matrix for use in calculations, using resistance list inputs

    # Determining signage of D array elements via predetermined system based on the initial direction chosen by user for currents w.r.t. node 1
    if direction_values[0] == "in":
      d11 = -1
      d31 = 1
    else:
      d11 = 1
      d31 = -1

    if direction_values[1] == "in":
      d22 = -1
      d32 = 1
    else:
      d22 = 1
      d32 = -1

    if direction_values[2] == "in":
      d13 = -1
      d23 = 1
      d33 = 1
    else:
      d13 = 1
      d23 = -1
      d33 = -1

    D = numpy.array([[d11, 0, d13],
               [0, d22, d23],
               [d31, d32, d33]])  # Defining D matrix for use in calculations based off of previously conditions
    A = numpy.multiply(R, D)  # Creates constant matrix A
    b = numpy.array([voltage_values[0], -1*voltage_values[1], 0])  #Creates vector b
    x = numpy.linalg.solve(A, b)  # Solving Matrix eqn Ax=b for vector x
    final_direction_values = [direction_values[0], direction_values[1], direction_values[2]]  # initialize list of final direction values

    # Evaluates the sign of the results from vector x to determine if the actual direction of the current within the circuit matches the initial direction chosen by user, and if not, reverses the direction of the currents
    if x[0] < 0:
      if direction_values[0] == "in":
        final_direction_values[0] = "out"
      else:
        final_direction_values[0] = "in"
    if x[1] < 0:
      if direction_values[1] == "in":
        final_direction_values[1] = "out"
      else:
        final_direction_values[1] = "in"
    if x[2] < 0:
      if direction_values[2] == "in":
        final_direction_values[2] = "out"
      else:
        final_direction_values[2] = "in"

    current_amps = numpy.absolute(x)
    current_amps = numpy.round(current_amps, 4)  # Final vector of current magnitudes, rounded
  except ValueError:
    print("Error with input lists, please try again")
    print("direction_values = 1x3 'in'/'out' list\n")
    print("voltage_values = 2x1 float list\n")
    print("resistance_values = 3x1 float list\n")
    sys.exit(1)  # Notifies user and exits program if there is an issue with input lists (specifially with the values in the input lists)
  except IndexError:
    print("Please ensure input lists are of the proper dimensions:\n")
    print("direction_values = 1x3 'in'/'out' list\n")
    print("voltage_values = 2x1 float list\n")
    print("resistance_values = 3x1 float list\n")
    sys.exit(1)  # Notifies the user and exits program if there is an issue with input lists (specifially with the dimensions of the input lists)
  return current_amps, final_direction_values


def plot_current_values(current_amps, final_direction_values):
  """Takes two lists of current magnitudes and directions, and creates graphic representing the directions of
  currents in the circuit with respect to Node 1 and labelling their values"""
  current_graph = plt.figure()

  if final_direction_values[0] == 'in':
    plt.arrow(-1,0,0.75,0, width=0.06)  # creates arrow into node for i1
  else:
    plt.arrow(0, 0, -0.75, 0, width=0.06)  # creates arrow out of node for i1
  if final_direction_values[1] == 'in':
    plt.arrow(1,0, -0.75,0, width=0.06)  # creates arrow into node for i2
  else:
    plt.arrow(0,0,0.75,0, width=0.06)  # creates arrow out of node for i2
  if final_direction_values[2] == 'in':
    plt.arrow(0,-1,0,0.75, width=0.06)  # creates arrow into node for i3
  else:
    plt.arrow(0,0,0,-0.75, width=0.06)  # creates arrow out of node for i3
  plt.plot(0,0,marker='o', color='black')  # creates point at node location
  plt.title("Node 1")  # Set graph title
  plt.annotate(f"i1 = {current_amps[0]} Amps", (-0.7, .05))  # labels arrow representing i1
  plt.annotate(f"i2 = {current_amps[1]} Amps", (.3, .05))  # labels arrow representing i2
  plt.annotate(f"i3 = {current_amps[2]} Amps", (.05, -.5))  # labels arrow representing i3
  plt.axis("off")  # turns off graph axes (not necessary, graph purely visual)
  return current_graph


if __name__ == "__main__":

  print("Program designed to evaluated simple circuit pictured below:\n")
  print("--------R1----*---R2--------\n"
        "|             |            |\n"
        "e1            R3           e2\n"
        "|             |            |\n"
        "----------------------------")
  print("\n")
  print("When prompted evaluate current directions with respect to node 1 as pictured below:\n")
  print("----i1----N1----i2----\n"
        "          |\n"
        "          i3\n"
        "          |\n")
  print("\n")

test_directions_1 = ['in', 'in', 'in']
test_voltages_1 = [10, 0.5]
test_resistances_1 = [4, 4, 4]
test_results_1 = calculate_current_values(test_directions_1, test_voltages_1, test_resistances_1)

test_directions_2 = ['in', 'in', 'in']
test_voltages_2 = [5, 10]
test_resistances_2 = [4, 2, 7]
test_results_2 = calculate_current_values(test_directions_2, test_voltages_2, test_resistances_2)

print(f"Test 1:\nTest with {test_directions_1} as input directions\n{test_voltages_1} as input voltages\n{test_resistances_1} as input resistances\n")

print(f"With respect to Node 1:\ni1 goes {test_results_1[1][0]}\ni2 goes {test_results_1[1][1]}\ni3 goes {test_results_1[1][2]}\nThe current values are:\ni1 = {test_results_1[0][0]} amps\ni2 = {test_results_1[0][1]} amps\ni3 = {test_results_1[0][2]} amps")
print("\n")

print("Test 2: Verify that function direction output remains constant regardless of initial directions chosen by user, using same voltage/resistance values as Test 1 but varying input directions\n")
test_directions_1_variations = [['in', 'in', 'in'], ['in', 'in', 'out'], ['in', 'out', 'in'], [ 'in', 'out', 'out'], ['out', 'in', 'in'], ['out', 'in', 'out'], ['out', 'out', 'in'], ['out', 'out', 'out']]
for i in test_directions_1_variations:
  print(f'{i} --> {calculate_current_values(i, test_voltages_1, test_resistances_1)[1]}')

plot_current_values(test_results_1[0], test_results_1[1])
plot_current_values(test_results_2[0], test_results_2[1])
plt.show()