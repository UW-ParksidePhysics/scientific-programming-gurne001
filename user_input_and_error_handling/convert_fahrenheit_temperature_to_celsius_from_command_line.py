from sys import (argv, exit)

def temp_f_to_c(x):
  return (x - 32) * (5 / 9)

try:
  temperature = float(argv[1])
except:
  print('Must provide a temperature as a command-line argument') #prints message if no command-line argument is provided
  exit(1) #exits program

temperature_celsius = temp_f_to_c(temperature)

print(f'{temperature} degrees Fahrenheit is {temperature_celsius} degrees Celsius')