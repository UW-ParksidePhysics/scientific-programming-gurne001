def temp_f_to_c(x):
  return (x - 32) * (5 / 9)

temperature = float(input("Enter temperature in Fahrenheit: "))
temperature_celsius = temp_f_to_c(temperature)

print(f'{temperature} degrees Fahrenheit is {temperature_celsius} degrees Celsius')