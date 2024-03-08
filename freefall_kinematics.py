from math import sqrt

def velocity(time, initial_velocity, gravitational_acceleration):
  return initial_velocity - gravitational_acceleration * time


def height(time, initial_height, initial_velocity, gravitational_acceleration):
  return initial_height + initial_velocity * time - 0.5 * gravitational_acceleration * time ** 2


def velocity_square(height, initial_height, initial_velocity, gravitational_acceleration):
  return initial_velocity ** 2 - 2 * gravitational_acceleration * (height - initial_height)


def time(height, initial_height, initial_velocity, gravitational_acceleration):
  time_to_max_height = initial_velocity/gravitational_acceleration
  discriminant = (time_to_max_height**2) - 2*(height - initial_height)/gravitational_acceleration
  if discriminant < 0:
    print("Error: Negative value in square root")
    return None
  else:
    return time_to_max_height + sqrt(discriminant)


if __name__ == "__main__":
  # Test Velocity function:
  # t=2 v0=1, g=9.8 --> v(t)=-18.6
  print(f'Final velocity is {velocity(2, 1, 9.8)} when time=2, initial velocity=1, and gravitational acceleration=9.8')
  # Test Height function: