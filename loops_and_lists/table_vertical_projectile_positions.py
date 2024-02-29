gravitational_accel_uranus = 9.01
gravitational_accel_titan = 1.3455
initial_velocity = 25
n = 10

def vertical_position(t, g, velocity=initial_velocity):
  """
  Returns the vertical position of a projectile at time t with respect to particular gravity g"""
  vertical_position = velocity*t - (g*t**2)/2
  return vertical_position

time_uranus = 0
time_titan = 0
max_uranus = (2*initial_velocity)/gravitational_accel_uranus
max_titan = (2*initial_velocity)/gravitational_accel_titan
interval_uranus = max_uranus/n
interval_titan = max_titan/n
line_break = "-------------------------------------------------"

print('For initial velocity of 25 m/s:')
print(line_break)
print(f'Uranus (g = {gravitational_accel_uranus} m/s^2) Titan (g = {gravitational_accel_titan} m/s^2)')
print(line_break)
print('      t(s)        y(m)        t(s)        y(m)')
print(line_break)
print("Using a 'for' loop:")
for i in range(n+1):
  print(f'{time_uranus:11.4f} {vertical_position(time_uranus, gravitational_accel_uranus):11.4f} {time_titan:11.4f} {vertical_position(time_titan, gravitational_accel_titan):11.4f}')
  time_uranus += interval_uranus
  time_titan += interval_titan

print("Using a 'while' loop:")
x = 0
time_uranus = 0
time_titan = 0

while x <= 10:
  print(f'{time_uranus:11.4f} {vertical_position(time_uranus, gravitational_accel_uranus):11.4f} {time_titan:11.4f} {vertical_position(time_titan, gravitational_accel_titan):11.4f}')
  time_uranus += interval_uranus
  time_titan += interval_titan
  x += 1