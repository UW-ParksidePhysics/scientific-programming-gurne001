import numpy
import math
import matplotlib.pyplot as plt

#Goal is to evaluate simple multiloop circuit a la PHYS202; where there are 2 power sources, 3 resistors, and the power sources and resistance values are known.

#Establishes directions for proper input values for coming section
print("Input current directions based on Node 1 layout for the purpose of circuit evaluation, please input 'in' or 'out'")

current_directions = ['placeholder', 'placeholder', 'placeholder']
valid_input = False
while not valid_input:
  valid_input = True
  for i in range(0,3):
    current_value = input(f"Evaluate with i{i+1} directed in/out of node N1: ")
    if current_value == "in" or current_value == "out":
      current_directions[i]=(current_value)
    else: 
      print("Invalid input, please enter 'in' or 'out'")
      valid_input = False


print("Next, input values for voltages/resistances for the purpose of circuit evaluation")
voltages = [0,0]
resistances = [0,0,0]
valid_input = False
while not valid_input:
  valid_input = True
  for i in range(0,2):
    voltage_value = float(input(f"e{i+1} voltage (in volts): "))
    # if not voltage_value.isnumeric():
    #   print("Invalid input, please enter a number")
    #   valid_input = False
    # else:
    voltages[i] = (voltage_value)


valid_input = False
while not valid_input:
  valid_input = True
  for i in range(0,3):
    resistance_value = float(input(f"R{i+1} resistance (in ohms): "))
    # if not resistance_value.isnumeric():
    #   print("Invalid input, please enter a number")
    #   valid_input = False
    # else:
    resistances[i] = (resistance_value)

#Array of constant values for given R's in previous section, last row placeholder 1's for ease of later multiplication with array D for purposes of sign determination
R=numpy.array([[resistances[0], 0, resistances[2]],[0, resistances[1], resistances[2]], [1, 1, 1]])

#Determining signage of D array elements via predetermined system based on direction of analysis for loop/node eqns
if current_directions[0] == "in":
  d11 = -1
  d31 = 1
else:
  d11 = 1
  d31 = -1

if current_directions[1] == "in":
  d22 = -1
  d32 = 1
else:
  d22 = 1
  d32 = -1

if current_directions[2] == "in":
  d13 = -1
  d23 = 1
  d33 = 1
else:
  d13 = 1
  d23 = -1
  d33 = -1

#Array that accounts for effect of chosen current directions on resulting system of eqns
D=numpy.array([[d11, 0, d13], [0, d22, d23], [d31, d32, d33]])

#Multiply R and D to derive constant coeff matrix for purpose of matrix eqn Ax=b
A=numpy.multiply(R, D)

#b vector containing the voltages of each power source, used for solving linear system
b=numpy.array([voltages[0], -1*voltages[1], 0])

x=numpy.linalg.solve(A, b)

#Evaluates sign of given current values to determine if direction of currents guessed in earlier portion of program needs to be reversed
if x[0] < 0:
  if current_directions[0] == "in":
    current_directions[0] = "out"
  else:
    current_directions[0] = "in"

if x[1] < 0:
  if current_directions[1] == "in":
    current_directions[1] = "out"
  else:
    current_directions[1] = "in"

if x[2] < 0:
  if current_directions[2] == "in":
    current_directions[2] = "out"
  else:
    current_directions[2] = "in"

#Takes absolute value of x vector as signage irrelevant beyond indication of proper direction, which was just addressed
current_amps = numpy.absolute(x)

print(f'With respect to Node 1, i1 goes {current_directions[0]}, i2 goes {current_directions[1]}, i3 goes {current_directions[2]}\nThe current values are:\ni1 = {current_amps[0]} amps, i2 = {current_amps[1]} amps, i3 = {current_amps[2]} amps')