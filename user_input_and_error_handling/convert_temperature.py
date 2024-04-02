"""This module allows for conversion of temperatures between Celsius, Kelvin, and Fahrenheit in any order.

Example inputs/outputs:
>>> temp.celsius_to_fahrenheit(0)
32.0
>>> temp.fahrenheit_to_celsius(32)
0.0
>>> temp.celsius_to_kelvin(0)
273.15"""

import sys

#make six conversion functions btwn c,k,f

def celsius_to_fahrenheit(celsius_temperature):
  return (celsius_temperature*(9/5)) + 32

def celsius_to_kelvin(celsius_temperature):
  return celsius_temperature + 273.15

def fahrenheit_to_celsius(fahrenheit_temperature):
  return (fahrenheit_temperature - 32) * (5/9)

def fahreheit_to_kelvin(fahrenheit_temperature):
  return (fahrenheit_temperature - 32) * (5/9) + 273.15

def kelvin_to_celsius(kelvin_temperature):
  return kelvin_temperature - 273.15

def kelvin_to_fahrenheit(kelvin_temperature):
  return (kelvin_temperature - 273.15) * (9/5) + 32


if __name__ == "__main__":
  def test_conversion():
    fahrenheit = 32
    celsius = 0
    kelvin = 273.15
    def test_tolerance(a, b, tolerance=1e-6):
      """Return 'True' if a == b within tolerance"""
      return abs(a - b) < tolerance
    success = test_tolerance(celsius_to_fahrenheit(fahrenheit_to_celsius(fahrenheit)), fahrenheit) and \
    test_tolerance(kelvin_to_celsius(celsius_to_kelvin(celsius)), celsius) and \
    test_tolerance(kelvin_to_fahrenheit(fahreheit_to_kelvin(fahrenheit)), fahrenheit)
    message = "Test failed"
    assert success, message
    print("Test passed")

if len(sys.argv) == 2 and sys.argv[1] == "verify":
  test_conversion()

def conversion(temperature, scale):
  if scale == "C":
    return f'{celsius_to_fahrenheit(temperature)} F, {celsius_to_kelvin(temperature)} K'
  elif scale == "F":
    return f'{fahrenheit_to_celsius(temperature)} C, {fahreheit_to_kelvin(temperature)} K'
  elif scale == "K":
    return f'{kelvin_to_celsius(temperature)} C, {kelvin_to_fahrenheit(temperature)} F'
  else:
    print("Please enter a valid scale, C/F/K")
    return None

if len(sys.argv) == 3:
  print(conversion(float(sys.argv[1]), sys.argv[2]))