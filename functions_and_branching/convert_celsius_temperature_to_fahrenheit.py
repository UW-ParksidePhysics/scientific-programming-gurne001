def convert_fahrenheit_temperature_to_celsius(fahrenheit_temperature):
  """Converts a temperature from Fahrenheit to Celsius."""
  return (fahrenheit_temperature - 32) * (5 / 9)

def convert_celsius_temperature_to_fahrenheit(celsius_temperature):
  """Converts a temperature from Celsius to Fahrenheit."""
  return (celsius_temperature * (9 / 5)) + 32

if __name__ == "__main__":
  test_temps_celsius = [0, 21, 100]
  test_temps_fahrenheit = [32, 69.8, 212]
  print('Input\t\tOutput')
  print("----------------------")
  for celsius_temp in test_temps_celsius:
    converted_temperature = convert_fahrenheit_temperature_to_celsius(convert_celsius_temperature_to_fahrenheit(celsius_temp))
    print(f'{celsius_temp:6}\t\t{converted_temperature:6.0f}')
