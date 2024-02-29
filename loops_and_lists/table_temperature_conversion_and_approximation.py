#Establish Variables before referencing them in loop
degrees_fahrenheit = 0
degrees_celsius = 0
approximate_degrees_celsius = 0
print('   F      C     ~C') #3 spaces before F to match width of field in loop, 6 before C for same reason, only 5 spaces before ~C for same reason
while degrees_fahrenheit <= 100:
  degrees_celsius = (degrees_fahrenheit - 32) * 5 / 9
  approximate_degrees_celsius = (degrees_fahrenheit - 30)/2
  print(f' {degrees_fahrenheit:3d} {degrees_celsius:6.1f} {approximate_degrees_celsius:6.0f}')
  degrees_fahrenheit += 20