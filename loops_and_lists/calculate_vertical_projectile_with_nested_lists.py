times_uranus = []
times_titan = []
heights_uranus = []
heights_titan = []

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

for i in range(n+1):
  times_uranus.append(time_uranus)
  times_titan.append(time_titan)
  heights_uranus.append(vertical_position(time_uranus, gravitational_accel_uranus))
  heights_titan.append(vertical_position(time_titan, gravitational_accel_titan))
  time_uranus += interval_uranus
  time_titan += interval_titan

times_positions = [times_uranus, heights_uranus, times_titan, heights_titan]

line_break = "-------------------------------------------------"

print('For initial velocity of 25 m/s:')
print(line_break)
print(f'Uranus (g = {gravitational_accel_uranus} m/s^2) Titan (g = {gravitational_accel_titan} m/s^2)')
print(line_break)
print('        t(s)      y(m)       t(s)       y(m)')
print(line_break)

for i in range(n+1):
  for j in range(4):
    if j<3:
      print(f'{times_positions[j][i]:11.2f}', end='')
    else:
      print(f'{times_positions[j][i]:11.2f}')


time_positions = []
for i in range(n+1):
  row_j = []
  for j in range(4):
    row_j.append(times_positions[j][i])
  time_positions.append(row_j)


print('\n\nFor initial velocity of 25 m/s:')
print(line_break)
print(f'Uranus (g = {gravitational_accel_uranus} m/s^2) Titan (g = {gravitational_accel_titan} m/s^2)')
print(line_break)
print('        t(s)      y(m)       t(s)       y(m)')
print(line_break)

for i in range(n+1):
  for j in range(4):
    if j<3:
      print(f'{time_positions[i][j]:11.2f}', end='')
    else:
      print(f'{time_positions[i][j]:11.2f}')


